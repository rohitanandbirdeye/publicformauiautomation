import asyncio
import os
from browser_use import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
load_dotenv()

task = """
    ### Navigate to yelp review page and extract reviews
    1. Go to the URL https://www.yelp.com/biz/browns-automotive-experts-albuquerque-2#reviews
    2. Wait for the page to load and display the reviews.
    3. Identify the table or structured data containing reviews. It's under review-summary section.
    4. Extract all rows and columns while preserving the relationship between data points
    5. For each review, extract the following details:
        - Review title
        - Review text
        - Star rating
        - Date of review
        - Reviewer name
        - Reviewer location
        - Review photo (if available)
    6. If pagination exists, navigate through at least the first 3 pages and extract all data
    7. Store the extracted data in a structured format (e.g., JSON, CSV, or database)
    8. Ensure that the data is clean and well-organized, with appropriate headers for each column
    9. If any errors occur during extraction, log them for review
    10. Ensure that the script is efficient and does not overload the server with requests
    11. If the script is successful, print "Data extraction completed successfully."
    12. If the script fails, print "Data extraction failed."

    ### Additional Instructions
     - Format the extracted data in a CSV-compatible format with appropriate headers. If any data points are missing, mark them as "N/A" rather than leaving them blank.

    
"""

async def main():
    agent = Agent(
        task=task,
        # llm = ChatOpenAI(
        #     model="gpt-4o",
        #     temperature=0.0,
        #     max_retries=2,
        #     timeout=30,
        # ),
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            #gemini_api_key="AIzaSyARVVhiSaqqGxS0nOowHjiub2MX0DprSFw"
        )
    )
    history = await agent.run()
    return history

asyncio.run(main())