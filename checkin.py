import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

task = """
   ### Prompt for checkin automation

**Objective:**
Visit [checkin](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/checkin/), fill the form and see results.

**Important:**
- Make sure that you click **submit** button.
---

### Step 1: Navigate to the Website
- Open [checkin](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/checkin/).

---

### Step 2: Click on "submit" Button
- Locate the **submit** button on the page.
- Click on the **submit** button.
- Form should not be submitted.
---

### Step 2: Fill the form with invalid data then click on "submit" Button
- Fill the form with the following details:
  - Keep Name field empty.
  - Email: *aitest@*
  - Phone: *1234567890*
- Click on the **submit** button.
- Form should not be submitted.
---

### Step 3: Fill the form and then click on "submit" Button
- Fill the form with the following details:
  - Name: **AI testing**
  - Email: *aitest@test.com*
- Click on the **submit** button.
- Form should be submitted.
---

Important:
        - Wait for each element to load before interacting
        - Use the correct locators for each element
        - Verify the submit button is clickable before clicking
        - Ensure efficiency and accuracy throughout the process
"""

async def main():
    agent = Agent(
        task=task,
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

asyncio.run(main())