import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

task = """
   ### Prompt for Review us contact us directly automation

**Objective:**
Visit [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1), click contact us directly button and see results.

**Important:**
- Make sure that you click "contact us direclty" button.
- After clicking the button, a new form will appear and you should fill out the form.
---

### Step 1: Navigate to the Website
- Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1).

---

### Step 2: Click on "Contact is directly" Button
- Locate the "contact is directly" button on the page.
- Click on the button.
- A new form should appear.
- Fill up the form random experience, name and dummy email address, check mark the check box that says i would like to be contacted.
- Submit the form.
---

### Step 3: Navigate to the Website again
- Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1).

### Step 4: Click on "Review us on Google" Button
- If the browser gets redirected then close the broswer window

---

### Step 5: Navigate to the Website 
- Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).

---

### Step 6: Select the star rating
- Click the Next button once star rating is given
- A new form should appear.
- Fill up the form based on the star rating selected with random experience, name and dummy email address, check mark the check box that says i would like to be contacted.
- Submit the form.

---


**Important:** Ensure efficiency and accuracy throughout the process."""

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