from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

task = """
   ### Navigate to checkin page and fill the form

    Here are the specific steps:
    1. go to url https://birdeye.com/dumpling-baby-china-bistro-165406729056862/checkin
    2. click on the **submit** button
    3. Form should not be submitted.
    4. Fill the form with the following details:
        - Name: **AI testing**
        - Email: *
    5. Click on the **submit** button
    6. Form should not be submitted.
    7. Fill the form with the following details:
        - Name: **AI testing**
        - Email: *aitest@test.com*
    8. Click on the **submit** button
    9. Form should be submitted.
    10. Verify the form submission by checking for a success message or confirmation.
    11. If the form submission is successful, print "Form submitted successfully."
    12. If the form submission fails, print "Form submission failed."

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
    history = await agent.run()
    return history

#asyncio.run(main())