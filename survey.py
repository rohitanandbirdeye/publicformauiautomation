
import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

surveyPrompt1 = """
   ### Prompt for surveys automation

   🧠 Task:
    You are a QA Automation Expert tasked with simulating how a real user would fill out and submit a multi-step survey on a webpage. Your job is to accurately identify and interact with all visible question types on the page, provide appropriate answers, then click the "Next" button to move forward. Continue this until the "Submit" button appears, and finally, submit the survey.

    **Objective:**
    Fill the survey form and leave a 3-star rating with the comment "Flexible timings might be a good idea!".

    Survey link: https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57465&businessId=172133591523666&source=preview

    🧾 Instructions (Step-by-step Behavior):
    Step 1: Open the survey URL in a browser - https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57465&businessId=172133591523666&source=preview.
    Step 2: First question "What is your gender?" is a multiple-choice question. Select the second option "Female".
    Step 3: The next question "Tell us about your experience" is a matrix radio button question. It wants to seek feedback of customer on 4 aspects of service like cleanliness, professionalism etc.
      - For the first row "Cleanliness", select the third option "Neutral" in its row of 4 radio buttons.
      - For the second row "Professionalism", select the third option "Neutral" in its row of 4 radio buttons.
      - For the third row "Time flexibility", select the third option "Neutral" in its row of 4 radio buttons.
      - For the fourth row "Ease of booking session", select the third option "Neutral" in its row of 4 radio buttons.
    Step 4: The next question is "Why did you visit us?" which is a multiple-choice question. Select the first and seocnd option "Purchase" and "Repair".
    Step 5: In the next question "Please rate us based on your experience?" you need to select a star rating.
       - The stars are enclosed in a div with class "rating-bubble-wrap". 
       - Inside this div, there are 5 stars. Each star is represented by a div with class "rating-star-block". 
       - Inside each star div, there is a icon with class "icon_phoenix-header-reviews" that contains the actual star icon.
       - The star icons and div is clickable. 
       - Hover over the 3rd star
       - Click on the third star (3-star rating) to give 3 stars
    Step 6: Beneath the star rating, there is a text input field "Leave us a review". Enter "Flexible timings might be a good idea!" in the text area.
    Step 7: Submit the survey by clicking the "Submit" button.
    Step 8: Wait until survey is successfully submitted. Log the text you can see after clicking the submit button."
    Step 9: Your task will complete once the survey is submitted and you see the message like this: "Thank you for your feedback!".

    🛑 Constraints:
    Do not reload the page.

    Do not skip any visible question.

    Do not fill hidden or disabled fields.

    Ensure that at least one option is selected for each question that requires it.

    For required fields, always provide a value.
"""

context = """
    You are using a browser automation agent to simulate end-user interaction with a survey form. The purpose is to validate the UI/UX and ensure that all question types behave as expected across multiple steps.

    The following are the types of survey questions you might encounter on each page:

    Multiple Choice (Checkboxes) – Select one or more options.

    Matrix Radio Button – For each row label (e.g., "Service", "Cleanliness"), select the appropriate radio button from a set of options like:
    "Excellent" | "Good" | "Fair" | "Poor".

    Matrix Dropdowns – For each row label, choose an answer from a dropdown (similar options as above).

    Matrix Ratings – For each row, select a rating from a scale of options (e.g., 1–5 stars or circles).

    Text Inputs – Answer using either short input fields or multi-line textareas.

    Contact Information – Fill out fields like Full Name, Email, Phone Number (US format).

    Datepicker – Select a valid date for questions like “When did you visit us?”

    Rating Scale (1–10) – Choose a value between 1 to 10 by clicking on the corresponding rating bubble.
"""

surveyPrompt2 = """
   ### Prompt for surveys automation

   🧠 Task:
    You are a QA Automation Expert tasked with simulating how a real user would fill out and submit a multi-step survey on a webpage. Your job is to accurately identify and interact with all visible question types on the page, provide appropriate answers, then click the "Next" button to move forward. Continue this until the "Submit" button appears, and finally, submit the survey.

    **Objective:**
    Fill the survey form and select your date of visit in the end date picker as "05-05-2025".

    Survey link: https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57471&businessId=172133591523666&source=preview

    🧾 Instructions (Step-by-step Behavior):
    Step 1: Open the survey URL in a browser - https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57471&businessId=172133591523666&source=preview.
    Step 2: The next question "Tell us about your experience" is a matrix dropdown question. It wants to seek feedback of customer on 3 aspects of service.
      - For the first row "Cleanliness", click the 'Select' dropdown, wait for dorpdown to open, select the third option "Neutral" from the dropdown next to it. Wait for it to close before moving to the next dropdown
      - For the second row "Professionalism", click the 'Select' dropdown, wait for dorpdown to open, select the third option "Neutral" from the dropdown next to it. Wait for it to close before moving to the next dropdown
      - For the third row "Ease of booking online", click the 'Select' dropdown, wait for dorpdown to open, select the third option "Neutral" from the dropdown next to it. Wait for it to close before moving to the next dropdown
    Step 3: The next question is "What is your gender?" which is a dropdown of multiple choices. Click the Select dropdow under it and select the third option "frog" from the dropdown.
    Step 4: The next question is again mamtrix type of "Employee feedback". You need to select a number for each aspect of the employees and either agree or disagree between the scale of *Strongly Disagree (1) to Strongly Agree (5)*.
        - For "Receptionist" was helpful select *3* in front of it
        - For "Engineers guided you on all steps" select *4* in front of it
        - For "You felt welcome" select *4* in front of it
    Step 5: The next question What was your date of visit? is a date picker.
         - Click on it and wait for the date picker to open.
         - Select the date "05-05-2025" from the date picker.
         - Wait for datepicker to close
    Step 6: Submit the survey by clicking the "Submit" button.
    Step 7: Wait until survey is successfully submitted. Log the text you can see after clicking the submit button."
    Step 8: Your task will complete once the survey is submitted and you see the message like this: "Thank you for your feedback!".

    🛑 Constraints:
    Do not reload the page.

    Do not skip any visible question.

    Do not fill hidden or disabled fields.

    Ensure that at least one option is selected for each question that requires it.

    For required fields, always provide a value.
"""

#We can reuse this function with different prompts for example: check if validation is working if a mandatory question is skipped 
async def runAutomation(prompt):
    agent = Agent(
        task=prompt,
        message_context=context,
        llm=ChatOpenAI(model="gpt-4o")
    )
    await agent.run()

asyncio.run(runAutomation(surveyPrompt1))

