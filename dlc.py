import os
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

task = """
   ### Navigate to DLC register page and fill the form

    Here are the specific steps:
    1. go to url https://publicforms-test.birdeye.com/dlc/register/MTcxODc5NDQ4MjY0MjA0
    2. click on the **submit** button
    3. Validation errors should be visible on page.
    4. The following errors should be visible:
        - **Registration Id Number**: This field is required.
        - **Registration Id Type**: This field is required.
        - **Address line 1**: This field is required.
        - **Legal Business Name**: This field is required.
    5. If errors are not visible on page, then the form is not working as expected. Throw error and exit.
    6. Form should not be submitted.

    Important:
      - Wait for each element to load before interacting
      - Use the correct locators for each element
      - Verify the submit button is clickable before clicking
      - Ensure efficiency and accuracy throughout the process
"""

async def main():
    agent = Agent(
        task=task,
        enable_memory=False,
        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.0,
            max_retries=2,
            timeout=30,
        )
    )
    history = await agent.run()
    print('------------------------')
    print(history.is_successful())
    print('------------------------')
    print(history.final_result())
    print('------------------------')

asyncio.run(main())