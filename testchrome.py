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

#https://github.com/browser-use/browser-use/issues/1520

browser = Browser(
    config=BrowserConfig(
        headless=False,
        browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        extra_browser_args=[
             "--user-data-dir=remote-debug-profile",
            #"--user-data-dir=/Users/anand/Library/Application Support/Google/Chrome/Default",  # Path to Chrome user data
            #"--profile-directory=Profile 1"  # Specify the profile directory (e.g., Default, Profile 1, etc.)
        ]
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