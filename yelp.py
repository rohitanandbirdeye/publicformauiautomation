import asyncio
import os
from browser_use import Agent, Browser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from browser_use.browser.context import BrowserContextConfig, BrowserContext

load_dotenv()

config = BrowserContextConfig(
    #cookies_file="path/to/cookies.json",
    wait_for_network_idle_page_load_time=3.0,
    window_width=1280,
    window_height=1100,
    locale='en-US',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    highlight_elements=True,
    viewport_expansion=500,
    allowed_domains=['*'],
)

browser = Browser()
context = BrowserContext(browser=browser, config=config)

task = """
    ### Navigate to indeed review page and extract reviews
    1. Go to the URL https://www.indeed.com/cmp/Marlo-Furniture/reviews
    2. Solve the captcha, don't navigate to the page or another url until the captcha is solved
    3. Wait for the page to load and display the reviews.
    4. Identify the table or structured data containing reviews. It's under review-summary section.
    5. Extract all rows and columns while preserving the relationship between data points
    6. For each review, extract the following details:
        - Review title
        - Review text
        - Star rating
        - Date of review
        - Reviewer name
        - Reviewer location
        - Review photo (if available)
    7. If pagination exists, navigate through at least the first 3 pages and extract all data
    8. Store the extracted data in a structured format (e.g., JSON, CSV, or database)
    9. Ensure that the data is clean and well-organized, with appropriate headers for each column
    10. Save the data in a JSON file named "yelp_reviews.json" in the current directory
    11. If any errors occur during extraction, log them for review
    12. Ensure that the script is efficient and does not overload the server with requests
    13. If the script is successful, print "Data extraction completed successfully."
    14. If the script fails, print "Data extraction failed."
    
"""

async def main():
    agent = Agent(
        browser_context=context,
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