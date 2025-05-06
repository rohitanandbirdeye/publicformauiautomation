import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

task = """
   ### Prompt for checkin automation

**Objective:**
Visit [checkin](https://birdeye.com/dumpling-baby-china-bistro-1654067290565862/checkin/), fill the form and see results.

**Important:**
- Make sure that you click **submit** button.
---

### Step 1: Navigate to the Website
- Open [checkin](https://birdeye.com/dumpling-baby-china-bistro-1654067290565862/checkin/).

---

### Step 2: Click on "submit" Button
- Locate the **submit** button on the page.
- Click on the **submit** button.
- Form should not be submitted.
---

### Step 2: Fill the form and then click on "submit" Button
- Fill the form with the following details:
  - Name: **AI testing**
  - Email: *aitest@test.com*
- Click on the **submit** button.
- Form should be submitted.
---

**Important:** Ensure efficiency and accuracy throughout the process."""

async def main():
    os.environ["GOOGLE_API_KEY"]="AIzaSyAFw8PMvF8Ot16Ek7MmyIwvriLDrBpbjA0"
    agent = Agent(
        task=task,
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
    )
    await agent.run()

asyncio.run(main())