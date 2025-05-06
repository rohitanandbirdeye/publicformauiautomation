import os
from langchain_ollama import ChatOllama
from browser_use import Agent, Browser, BrowserConfig
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

# llm=ChatOllama(model="qwen2.5", num_ctx=32000)
llm=ChatOllama(model="llama4", num_ctx=1000)

async def main():
    agent = Agent(
        task=task,
        llm =llm,
        # browser=browser
    )
    await agent.run()

asyncio.run(main())