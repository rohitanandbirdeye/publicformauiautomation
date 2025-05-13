import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

task = """
   ### Navigate to checkin page and fill the form

    Here are the specific steps:
    1. go to url https://app.birdeye.com/dashboard/home
    2. Click on **Social AI** on the left side of the page
    
"""

browser = Browser(
    config=BrowserConfig(
        headless=False,
        # Specify the path to your Chrome executable
        browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome',
        #browser_binary_path='/Applications/Safari.app/Contents/MacOS/Safari',  # macOS path
    )
)

async def main():
    agent = Agent(
        task=task,
        browser=browser,
        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.0,
            max_retries=2,
            timeout=30,
        )
    )
    history = await agent.run()
    await browser.close()

asyncio.run(main())