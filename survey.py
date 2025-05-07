
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

#https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57413&businessId=172133591523666&source=preview

surveyUrl = "https://app.birdeye.com/JYSK-174369104409479/survey?surveyId=57123&businessId=174369104409479&source=preview"

completeSurveyPrompt = """
   ### Prompt for surveys automation

**Objective:**

Visit the below given URL and fill out the survey form. The survey consists of multiple questions, including multiple-choice and open-ended questions.
The goal is to automate the process of filling out the survey form.

**Instructions:**
- Answer each question considering a positive experience with the product/service
- The survey may contain multiple-choice questions, rating scales, and open-ended questions.
- The survey might contain dummy answer options, so please select the most relevant ones.
- After answering each question, if more questions are available, click the "Next" button to proceed. Ensure Next button is present in the screen and is clicakble and clicked only after answering the current question.
- If the survey contains a "Submit" button, click it after answering all questions.
- If the survey contains a "Finish" button, click it after answering all questions.
- Ensure that the progress bar in the footer of the survey is updated correctly after each question.
- After each question is answered, check and log the progress bar to ensure it reflects the correct percentage of completion.

1. Navigate to the survey link: https://app.birdeye.com/JYSK-174369104409479/survey?surveyId=57123&businessId=174369104409479&source=preview

2. For rating questions (0-5 or 0-10 scales):
   - select the highest rating
   - each rating number on the scale is enclosed in a div of class "rating-bubble" with the data-value attribute representing the rating value. dont get confused with the divs that are not enclosed in the "rating-bubble" class.

3. For multiple-choice questions, select options that align with:
    - Positive aspects of the experience
    - Features that were most useful
    - Aspects that made the experience enjoyable

4. For single-choice radio type questions, select any radio options.

5. For open-ended questions, write thoughtful responses:

6. Demographic questions (if asked):
   - Fill in basic information without sharing unnecessarily sensitive details
   - Skip optional demographic questions unless specifically instructed to complete them

Complete the survey honestly but constructively, providing feedback that would be helpful for
Important:
        - Reindex elements after each question is answered - since page and DOM will change
        - Wait for each element to load before interacting - especially the rating buttons (0-10)
        - Use the correct locators for each element - especially the rating and radio buttons (0-10)
        - Ensure efficiency and accuracy throughout the process
        - If any element is not found, log the error and continue with the next element
        - In case the survey contains any other type of question, please answer them by recognizing the context of the survey

Final Step:
After executing and submitting the survey, log your feedback on the user experience. Log any errors or issues encountered during the process.
"""

#We can reuse this function with different prompts for example: check if validation is working if a mandatory question is skipped 
async def runAutomation(prompt):
    agent = Agent(
        task=prompt,
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            gemini_api_key=os.getenv("GOOGLE_API_KEY")
        )
    )
    await agent.run()

asyncio.run(runAutomation(completeSurveyPrompt))