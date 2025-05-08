import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

#https://birdeye.com/boqueron-172133591523666/review-us?rtype=review_request&rid=23931483625&nr=1&source=email&templateId=1118678&custId=lVN3EwoZ0gZfuWirOmVTCg%3D%3D&enc=1

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
- If the browser gets redirected



**Important:** Ensure efficiency and accuracy throughout the process."""

config = BrowserConfig(
    # headless=False,
    # disable_security=False,
    # browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    connect_over_cdp=True,
    launch_args=[],  # No need to launch again, just connect
    headless=False,
    cdp_url="http://localhost:9222",  # Explicit connection
)

browser = Browser(config=config)

# Token counting function
def count_tokens(prompt: str) -> int:
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model.count_tokens(prompt).total_tokens

async def main():
    print(f"🔢 Token count for task: {count_tokens(task)}\n")
    agent = Agent(
        task=task,
        # browser=browser,
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