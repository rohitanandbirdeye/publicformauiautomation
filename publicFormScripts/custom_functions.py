import asyncio
from browser_use import Agent, Browser, Controller, ActionResult
from langchain_openai import ChatOpenAI

controller = Controller()

task_date_fallback = """
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


@controller.action("Select date manually in calendar popup")
def fallback_date_picker(label_text: str, target_date: str) -> str:
    """
    Fallback custom function if agent fails to select a date.
    """
    try:
        print(f"\n[Custom Date Fallback] Trying to select {target_date} for field '{label_text}' manually.")

        # Example logic: You can guide the agent to click date input, locate calendar popup, select target date.
        # This could be enhanced further to do JavaScript execution if needed.

        # Provide a clear instruction back to agent via extracted_content
        action_instruction = f"""
        Locate the input field near label '{label_text}'.
        Click on it to open the date picker popup.
        In the calendar popup, look for the date '{target_date}' and click on it.
        Ensure you do not type the date directly into the input box.
        After selecting the date, verify that the date is now displayed in the input.
        """
        return ActionResult(extracted_content=action_instruction)
    
    except Exception as e:
        return ActionResult(extracted_content=f"[Error in fallback_date_picker] {str(e)}")

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


async def run_with_fallback(task: str):
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o"),
        controller=controller
    )
    
    # Run the agent and capture the result
    result = await agent.run()
    
    # Fallback condition:
    if (
        not result
        or not getattr(result, 'extracted_content', '').strip()
    ):
        print("\n[Fallback Triggered] Agent failed to select the date properly or no result. Triggering custom fallback_date_picker.")
        # Call your custom fallback date picker
        fallback_result = fallback_date_picker(label_text="Visit Date", target_date="May 5, 2025")
        print(f"\n[Fallback Answer] {fallback_result.extracted_content}")
    else:
        print(f"\n[Agent Answer] {result.extracted_content}")

async def main():
    await run_with_fallback(task_date_fallback)

asyncio.run(main())