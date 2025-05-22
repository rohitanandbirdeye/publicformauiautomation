import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()


task = """
   ### Prompt for Social landing website page automation

    **Objective:**
    Visit https://birdeye.com/social-media-management-software/ and click button.

    ### Step 1: Navigate to the Website
    - Open https://birdeye.com/social-media-management-software/

    ---

    ### Step 2: watch video
    - Click on watch video button.
    - page should navigate to https://birdeye.com/free-demo/?ref=social
    - Navogate back to https://birdeye.com/social-media-management-software/
    - wait for page to load.
    ---

    ### Step 3: Click on "try social for free" Button
    - Click on "try social for free" Button
    - page should navigate to https://birdeye.com/social-media-management-free-trial/
    - Click "start your 30 day free trial" button.
    - Form should not be submitted.
    ---


    **Important:** Ensure efficiency and accuracy throughout the process.
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
    history = await agent.run()
    return history

asyncio.run(main())