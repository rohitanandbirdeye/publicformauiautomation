import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

task = """
   ### Prompt for Review us contact us diretly automation

**Objective:**
Visit [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1), click contact us directly button and see results.

**Important:**
- Make sure that you click "contact us direclty" button.
- After clicking the button, a new form will appear and you should fill out the form.
---

### Step 1: Navigate to the Website
- Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1).

---

### Step 2: Click on "contact is directly" Button
- Locate the "contact is directly" button on the page.
- Click on the button.
- A new form should appear.
- Close the browser window after form displays.
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