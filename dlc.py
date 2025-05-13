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
        - **First Name**: This field is required.
        - **Last Name**: This field is required.
        - **Email**: This field is required.
        - **Phone Number**: This field is required.
        - **Business Name**: This field is required.
        - **Business Address**: This field is required.
        - **City**: This field is required.
        - **State**: This field is required.
        - **Zip Code**: This field is required.
        - **Business Type**: This field is required.
        - **Business Website**: This field is required.
        - **Business Phone Number**: This field is required.
        - **Business Email**: This field is required.
        - **Business Description**: This field is required.
        - **Business Owner First Name**: This field is required.
        - **Business Owner Last Name**: This field is required.
    5. If no errors are visible, then the form is not working as expected.
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
        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.0,
            max_retries=2,
            timeout=30,
        )
    )
    await agent.run()

asyncio.run(main())