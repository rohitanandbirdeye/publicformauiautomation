
# import os
# from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
# from browser_use import (
#     Agent,
#     Browser,
#     BrowserConfig,
#     Controller,
#     ActionResult
# )
# import asyncio
# from dotenv import load_dotenv
# load_dotenv()

# browser = Browser(
#     config=BrowserConfig(
#       # headless=False,
#       # browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # Update this path based on your OS
#       # extra_browser_args=[
#       #     '--user-data-dir=/Users/adarsh.tiwari/Library/Application Support/Google/Chrome',  # Update this path based on your OS
#       #     '--profile-directory=Default'
#       # ])
#       connect_over_cdp=True,
#       cdp_url="http://localhost:9242",
#       reuse_existing=True,
#     )
# )

# task1 = """
# ### Prompt for Opening the Social Module in Birdeye web app

# **Objective:**
# Visit the provided Birdeye dashboard URL and open the **Social** module. Prioritize accuracy over speed.

# Don't retry unnecessarily, and avoid unnecessary clicks. If a question is not visible or interactable, skip it and move on to the next one.

# ---

# ### Step 1: Navigate to the Dashboard
# - Open [https://app.birdeye.com/dashboard/home](https://app.birdeye.com/dashboard/home).
# - Wait for the dashboard and left navigation menu to fully load.
# - My internet is slow, so please be patient until the page is fully loaded and loader is gone.

# ---

# ### Step 2: Locate the Social Module
# - In the left navigation menu, find the **Social** module.
# - Click on **Social** to open the module.
# - Wait for the Social module to load completely.

# ### Step 3: SUmmarise what the social module is about
# - Provide a brief summary of the Social module's purpose and features.

# ---

# ### Notes:
# - Avoid clicking “Back” or refreshing the page.

# """

# #We can reuse this function with different prompts for example: check if validation is working if a mandatory question is skipped 
# async def runCreatePostAutomation(prompt):
#     agent = Agent(
#         task=prompt,
#         browser=browser,
#         llm=ChatOpenAI(model="gpt-4o")
#     )
#     await agent.run()

# async def navigate_to_social_module(agent):
#     prompt = """
#         ### Prompt for Opening the Social Module in Birdeye web app

#         **Objective:**
#         Visit the provided Birdeye dashboard URL and open the **Social** module. Prioritize accuracy over speed.

#         Don't retry unnecessarily, and avoid unnecessary clicks. If a question is not visible or interactable, skip it and move on to the next one.

#         ---

#         ### Step 1: Navigate to the Dashboard
#         - Open [https://app.birdeye.com/dashboard/home](https://app.birdeye.com/dashboard/home).
#         - Wait for the dashboard and left navigation menu to fully load.
#         - My internet is slow, so please be patient until the page is fully loaded and loader is gone.

#         ---

#         ### Step 2: Locate the Social Module
#         - In the left navigation menu, find the **Social** module.
#         - Click on **Social** to open the module.
#         - Wait for the Social module to load completely.

#         ### Step 3: SUmmarise what the social module is about
#         - Provide a brief summary of the Social module's purpose and features.

#         ---

#         ### Notes:
#         - Avoid clicking “Back” or refreshing the page.

#     """
#     await agent.run()

# asyncio.run(runCreatePostAutomation(task1))

import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

load_dotenv()

# Setup Browser with CDP (must start Chrome with debugging port 9242)
browser = Browser(
    config=BrowserConfig(
        connect_over_cdp=True,
        cdp_url="http://localhost:9222",
        reuse_existing=True,
    )
)

# Setup LLM only once
llm = ChatOpenAI(model="gpt-4o")

async def navigate_to_social_module():
    task = """
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

    ### Step 3: Summarise what the social module is about
    - Provide a brief summary of the Social module's purpose and features.

    ---
    Notes:
    - Avoid clicking “Back” or refreshing the page.
    """
    agent = Agent(
        task=task,
        browser=browser,
        llm=llm
    )
    await agent.run()

async def open_create_post():
    task = """
    ### Prompt for navigating the social module in Birdeye web app and clicking on the **Create Post +** button

    **Objective:**
    Visit the already open Birdeye social/publish dashboard URL and click on the **Create Post +** button. 
    Prioritize accuracy over speed.

    Don't retry unnecessarily, and avoid unnecessary clicks.

    ---

    ### Step 1: Navigate to the Open Dashboard tab
    - If the social/publish route is not already open then navigate to [https://app.birdeye.com/dashboard/social/publish](https://app.birdeye.com/dashboard/social/publish).
    - Wait for the Create Post screen to fully load.
    - My internet is slow, so please be patient until the page is fully loaded and loader is gone.

    ---

    ### Step 2: Type content into the Create Post text area in focus
    - Locate the text area where we can type the caption of our posts.
    - The text area is not a traditional text area, its in a nestedcomplex div. So you may need to use the browser's developer tools to inspect the element and find the correct way to interact with it.
    - Type the caption "This is a test post" into the text area.
    - Exit

    ---
    Notes:
    - Avoid clicking “Back” or refreshing the page, even if the page load is slow.
    """
    agent = Agent(
        task=task,
        browser=browser,
        llm=llm
    )
    await agent.run()

async def select_single_posting_channel():
    task = """
        ### Objective:
        In the Birdeye Create Post dashboard, select a Facebook posting account from the channel dropdown without repeating or deselecting actions.

        ---

        ### Step 1: Ensure the Create Post page is open
        - Go to https://app.birdeye.com/dashboard/social/publish/createpost if not already open.
        - Wait for the page and its loader to fully finish loading. My internet is slow—be patient.
        - Don’t refresh or click anything randomly.

        ---

        ### Step 2: Open the social channel dropdown
        - Locate the “Select channels” section near the social icons.
        - It’s a nested div-based UI, not a native dropdown—inspect accordingly.
        - Click to open and wait for all dropdown elements to load.
        - Ensure the list of channels/accounts appears.

        ---

        ### Step 3: Select the Facebook account
        - Tabs for different platforms (Facebook, Instagram, etc.) will be visible once the dropdown is open.
        - Facebook tab is default; wait for its accounts to load.
        - Select the first Facebook account if it’s not already selected.
        - Check for selected state via DOM/class.
        - Don’t click if already selected.
        - Log the selected account's name.
        - Close the dropdown only after confirming selection.

        ---

        ### Notes:
        - Avoid infinite selection loops—don’t keep clicking the same checkbox.
        - No retries unless selection visibly failed.
        - Reindex elements if DOM changes or failure occurs.
    """

    agent = Agent(
        task=task,
        browser=browser,
        llm=llm
    )
    await agent.run()

async def main():
    # await navigate_to_social_module()
    # await open_create_post()
    await select_single_posting_channel()
    
asyncio.run(main())

# OBSERVATIONS:
# Chrome in debug mode is extremely slow, so the agent is taking a lot of time to run on initial load.
# If page is already open, it is moderately fast.

### Step 5: Add text for facebook post
    # - Each tab above the text area will have a different text area for each platform.
    # - Click on the **Facebook** tab to switch to the Facebook text area.
    # - Wait for the Facebook text area to load completely.
    # - My internet is slow, so please be patient until the page is fully loaded and loader is gone.
    # - The text area is not a traditional text area, its in a nestedcomplex div. So you may need to use the browser's developer tools to inspect the element and find the correct way to interact with it.
    # - Type the caption "This is a test post" into the Facebook tab's text area.

    ### Step 4: Confirm visible tabs on top of text area:
    # - Locate the text area placed below the posting channel dropdown element
    # - The text area is not a traditional text area, its in a nestedcomplex div. So you may need to use the browser's developer tools to inspect the element and find the correct way to interact with it.
    # - On the top of the text area, there will be multiple tabs visible.
    # - The default tab will be **Initial Content**.
    # - Based on the selected account, there will be different tabs visible, along with **Initial Content**.
    # - Since we selected the Facebook account, there will be a **Facebook** tab visible on top of the text area.
    # - Confirm if the **Facebook** tab is visible on top of the text area.
    # - If the **Facebook** tab is visible, then the account selection is successful.