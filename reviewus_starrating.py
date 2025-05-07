import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

task = """
   ### Prompt for Review us star rating directly automation

**Objective:**
Visit [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1), select star rating and see results.

**Important:**
- Make sure that you select "Star rating" .
- After selecting the star rating, a new form will appear and you should fill out the form.
---

### Step 1: Navigate to the Website 
- Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).

---

### Step 2: Select the Star Rating
- Wait for the star rating section to load.
- Select the **first star** (1-star rating).
- Click the **"Next"** button to proceed.

---

### Step 3: Fill Out the Feedback Form
- Wait for the feedback form to appear after clicking "Next".
- Enter the following dummy details:
  - **Review/Comment**: "Service was very slow and food was cold."
  - **Name**: "Jane Doe"
  - **Email**: "janedoe123@example.com"
- Check the box that says **"I would like to be contacted."**

---

### Step 4: Submit and Exit
- Click the **"Submit"** button on the form.
- Wait for the confirmation or success message.
- Close the browser window.

---


**Important:** Ensure efficiency and accuracy throughout the process."""

task2 = """
### Prompt for Review Us Star Rating Automation

**Objective:**
Visit [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1), select a 1-star rating, fill out the review form, and submit it.

**Important:**
- Ensure you select the 1-star rating.
- After selecting the star rating and clicking "Next", a feedback form should appear.
- Fill out the form with dummy information and check the contact permission box.

---

### Step 1: Navigate to the Website
- Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1) in a browser.

---

### Step 2: Select the Star Rating
- Wait for the star rating section to load.
- Select the **first star** (1-star rating).
- Click the **"Next"** button to proceed.

---

### Step 3: Fill Out the Feedback Form
- Wait for the feedback form to appear after clicking "Next".
- Enter the following dummy details:
  - **Review/Comment**: "Service was very slow and food was cold."
  - **Name**: "Jane Doe"
  - **Email**: "janedoe123@example.com"
- Check the box that says **"I would like to be contacted."**

---

### Step 4: Submit and Exit
- Click the **"Submit"** button on the form.
- Wait for the confirmation or success message.
- Close the browser window.

---

**Important:** Ensure each UI element is visible before interacting. Complete all steps without skipping.
"""

async def main():
    agent = Agent(
        task=task,
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            gemini_api_key=os.getenv("GOOGLE_API_KEY")
        )
    )
    await agent.run()

asyncio.run(main())