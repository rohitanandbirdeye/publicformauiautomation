
import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import (
    Agent,
    Browser,
    BrowserConfig,
    Controller,
    ActionResult
)
import asyncio
from dotenv import load_dotenv
load_dotenv()

browser = Browser(
    config=BrowserConfig(
      # headless=False,
      # browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # Update this path based on your OS
      # extra_browser_args=[
      #     '--user-data-dir=/Users/adarsh.tiwari/Library/Application Support/Google/Chrome',  # Update this path based on your OS
      #     '--profile-directory=Default'
      # ])
      connect_over_cdp=True,
      cdp_url="http://localhost:9242",
      reuse_existing=True,
    )
)

task1 = """
### Prompt for Opening the Social Module in Birdeye web app

**Objective:**
Visit the provided Birdeye dashboard URL and open the **Social** module. Prioritize accuracy over speed.

Don't retry unnecessarily, and avoid unnecessary clicks. If a question is not visible or interactable, skip it and move on to the next one.

---

### Step 1: Navigate to the Dashboard
- Open [https://app.birdeye.com/dashboard/home](https://app.birdeye.com/dashboard/home).
- Wait for the dashboard and left navigation menu to fully load.
- My internet is slow, so please be patient until the page is fully loaded and loader is gone.

---

### Step 2: Locate the Social Module
- In the left navigation menu, find the **Social** module.
- Click on **Social** to open the module.
- Wait for the Social module to load completely.

### Step 3: SUmmarise what the social module is about
- Provide a brief summary of the Social module's purpose and features.

---

### Notes:
- Avoid clicking “Back” or refreshing the page.

"""

#We can reuse this function with different prompts for example: check if validation is working if a mandatory question is skipped 
async def runAutomation(prompt):
    agent = Agent(
        task=prompt,
        browser=browser,
        llm=ChatOpenAI(model="gpt-4o")
    )
    await agent.run()

asyncio.run(runAutomation(task1))