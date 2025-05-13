
import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import (
    Agent,
    Browser,
    Controller,
    ActionResult
)

import asyncio
from dotenv import load_dotenv
load_dotenv()
controller = Controller()

# use this controller in your agent config to select star ratings for survey. make this dynamic with a rating parameter
@controller.action('select star rating')
async def select_rating(url: str, browser: Browser):
    page = await browser.get_current_page()
    await page.evaluate('''
        () => {
            const stars = document.querySelectorAll('.rating-star-block');
            stars.forEach(star => star.click());
        }
    ''')
    msg = 'All stars have been selected'
    return ActionResult(extracted_content=msg)

task1 = """
### Prompt for Survey Automation Agent – Birdeye Customer Feedback Form

**Objective:**
Visit the provided Birdeye survey URL, fill out the form as a genuine customer would, and attempt to submit it. Select reasonable answers for each type of question using available UI controls. Ensure that all required questions are answered correctly. Your goal is to fill all questions with positive answers, e.g. ‘Very Satisfied’, ‘Excellent’, ‘5 out of 5’, and a recent valid date. Prioritize accuracy over speed.

Don't repeat steps unnecessarily, and avoid unnecessary clicks. If a question is not visible or interactable, skip it and move on to the next one.

---

### Step 1: Navigate to the Survey
- Open [https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57471&businessId=172133591523666&source=preview](https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57471&businessId=172133591523666&source=preview).
- Wait for the form to fully load.

---

### Step 2: Fill Out the Survey Form

#### Star Ratings
- For each question using a star rating (typically shown as a 1–5 star row), select **4 or 5 stars** to simulate a positive customer experience.

#### Dropdown Questions
- For dropdown-style questions (e.g., satisfaction levels), click to open the dropdown and select a reasonable positive option like:
  - “Very Satisfied”  
  - “Satisfied”  
  - Avoid “Neutral” or “Dissatisfied” unless required.
- The UI uses custom dropdowns built with span/div elements — to select options, you must first click the dropdown trigger, then click the appropriate visible option. Avoid using select_dropdown_option

#### Radio Button Questions
- For questions with radio buttons, choose the option that corresponds to “Yes,” “Strongly Agree,” or similarly positive feedback.

#### Text Area / Open-ended Questions
- For text fields like “Any improvements you’d like to suggest?”, enter a thoughtful, polite comment, e.g.:
  - “Great service overall. Perhaps clearer signage at checkout.”

#### Matrix Questions with Dropdowns
- For rows like “Cleanliness,” “Product Availability,” etc., select values from dropdowns that show satisfaction or positive experience.
- Example: Choose “Very Good” or “Excellent” where applicable.
- Use element labels (e.g. text near the dropdown like 'Cleanliness') to identify inputs instead of relying on numeric index.

#### Matrix Questions with Range Scale (1–5)
- If a row contains a Likert scale (e.g., 1 = Strongly Agree, 5 = Strongly Disagree), select **1** or **2** for a positive response.

#### Date Picker
When selecting the date, do not type directly into the date field. Instead, click the date input to open the calendar, then click the correct date (e.g., May 5, 2025) on the calendar UI. Avoid retrying input_text actions on the date field — it's a custom calendar, not a text input."

#### Contact Info (if required)
- Enter dummy but valid-looking information:
  - Name: "John Doe"
  - Email: "johndoe@example.com"
  - Phone: "+1-418-543-8090"

---

### Step 3: Validation Check
- Once all questions are answered:
  - Click the **Submit** button.
  - If submission fails, identify the missing or incorrectly filled question (there will be a visible error).
  - Fix it and retry.

---

### Step 4: Submission Confirmation
- If the form is submitted successfully, output the following:
  - **Confirmation Message** or redirect page content (if available).
  - Timestamp of submission.
  - Summary of values selected (optional).

---

### Notes:
- Avoid clicking “Back” or refreshing the page.
- Do not leave any required field blank.
- Use realistic and consistent answers across the survey.

"""

task2 = """
### Prompt for Survey Automation Agent – Birdeye Customer Feedback Form

**Objective:**
Visit the provided Birdeye survey URL, fill out the form as a genuine customer would, and attempt to submit it. Select reasonable answers for each type of question using available UI controls. Ensure that all required questions are answered correctly. Your goal is to fill all questions with positive answers, e.g. ‘Very Satisfied’, ‘Excellent’, ‘5 out of 5’, and a recent valid date. Prioritize accuracy over speed.

Don't repeat steps unnecessarily, and avoid unnecessary clicks. If a question is not visible or interactable, skip it and move on to the next one.

---

### Step 1: Navigate to the Survey
- Open [https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57465&businessId=172133591523666&source=preview](https://app.birdeye.com/JYSK-172133591523666/survey?surveyId=57465&businessId=172133591523666&source=preview).
- Wait for the form to fully load.

---

### Step 2: Fill Out the Survey Form

#### Dropdown Questions
- For dropdown-style questions (e.g., satisfaction levels), click to open the dropdown and select a reasonable positive option like:
  - “Very Satisfied”  
  - “Satisfied”  
  - Avoid “Neutral” or “Dissatisfied” unless required.
- The UI uses custom dropdowns built with span/div elements — to select options, you must first click the dropdown trigger, then click the appropriate visible option. Avoid using select_dropdown_option

#### Radio Button Questions
- For questions with radio buttons, choose the option that corresponds to “Yes,” “Strongly Agree,” or similarly positive feedback.

#### Star Ratings
- For each question using a star rating (typically shown as a row of 5 star icons), select **4 or 5 stars** to simulate a positive customer experience.
- USe function select_rating to select the star rating.

#### Text Area / Open-ended Questions
- For text fields like “Any improvements you’d like to suggest?”, enter a thoughtful, polite comment, e.g.:
  - “Great service overall. Perhaps clearer signage at checkout.”

#### Matrix Questions with Dropdowns
- For rows like “Cleanliness,” “Product Availability,” etc., select values from dropdowns that show satisfaction or positive experience.
- Example: Choose “Very Good” or “Excellent” where applicable.
- Use element labels (e.g. text near the dropdown like 'Cleanliness') to identify inputs instead of relying on numeric index.
- Select a value for each row before moving to the next question.

#### Matrix Questions with Range Scale (1–5)
- If a row contains a Likert scale (e.g., 1 = Strongly Agree, 5 = Strongly Disagree), select **1** or **2** for a positive response.
- Select a value for each row before moving to the next question.

#### Date Picker
When selecting the date, do not type directly into the date field. Instead, click the date input to open the calendar, then click the correct date (e.g., May 5, 2025) on the calendar UI. Avoid retrying input_text actions on the date field — it's a custom calendar, not a text input."

#### Contact Info (if required)
- Enter dummy but valid-looking information:
  - Name: "John Doe"
  - Email: "johndoe@example.com"
  - Phone: "+1-418-543-8090"

---

### Step 3: Validation Check
- Once all questions are answered:
  - Click the **Submit** button.
  - If submission fails, identify the missing or incorrectly filled question (there will be a visible error).
  - Fix it and retry.

---

### Step 4: Submission Confirmation
- If the form is submitted successfully, output the following:
  - **Confirmation Message** or redirect page content (if available).
  - Timestamp of submission.
  - Summary of values selected (optional).

---

### Notes:
- Avoid clicking “Back” or refreshing the page.
- Do not leave any required field blank.
- Use realistic and consistent answers across the survey.
- When new elements appear, re-evaluate which required fields have now loaded. Do not assume the previous indices still apply.
- Re-check DOM after scrolls or dynamic updates for any new visible elements.
- If an element click fails due to index not found, fall back to finding elements by text, label, or role.
- Confirm each required field has been visibly filled before submission.

"""

#We can reuse this function with different prompts for example: check if validation is working if a mandatory question is skipped 
async def runAutomation(prompt):
    agent = Agent(
        task=prompt,
        controller=controller,
        llm=ChatOpenAI(model="gpt-4o")
    )
    await agent.run()

asyncio.run(runAutomation(task2))

# Things to rememeber when writing prompts for public forms:
# - need to specify that the survey form uses stylized dropdowns built with div or span elements and not native select
# - The agent incorrectly asummes the format and semantic of certain web elements like date picker, radio buttons and drodpowns. Since we have custom implementations for all these, we need to specify that in the prompt
# - Using Gemini for surveys almost never worked as expected. It was either too slow or it would not be able to fill the form at all. GPT-4o is much better at this (though it requires some iterations).


