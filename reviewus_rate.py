import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

#https://birdeye.com/boqueron-172133591523666/review-us?rtype=review_request&rid=23931483625&nr=1&source=email&templateId=1118678&custId=lVN3EwoZ0gZfuWirOmVTCg%3D%3D&enc=1

task = """
   ### Prompt for Review us contact us directly automation

**Objective:**
Visit [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1) and submit form.

**Important:**
- Make sure that you click "star rating" button.
- After clicking the button, a new form will appear and you should fill out the form.
- Don't try alternatives or other methods to submit the form.
---

### Step 1: Navigate to the Website
- Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).

---

### Step 2: Click on "star rating button" Button
- Wait for the star rating section to load.
- Select the **first star** (1-star rating).
- Click the **"Next"** button.
- Wait for the feedback form to appear.
- Fill out the form using:
   - **Review Comments:** "The service was extremely slow, and the food arrived cold and tasteless."
   - Put a space at end of **Review Comments** text area.
   - Trigger **keyup** event on the **Review Comments** text area to ensure it is valid.
   - **Name:** "AI Agent Tester"
   - **Email:** "ai@agenttest.com"
- Put a space at end of **Review Comments** text area.
- Trigger **keyup** event on the **Review Comments** text area to ensure it is valid.
- Click the **submit** button
- Submit the form.

---

### Step 3: Successful Submission
- Confirm submission by looking for a confirmation message.
- Once new message appears, close the browser.

---

### Step 3: Unsuccessful Submission
- If form submission fails, check for any error messages.
- If the button does not enable after 15 seconds, **fail and exit**.
- close the browser.

---

**Important:** Ensure efficiency and accuracy throughout the process."""

async def main():
    agent = Agent(
        task=task,
        # llm = ChatGoogleGenerativeAI(
        #     model="gemini-1.5-flash",
        #     temperature=0,
        #     max_tokens=None,
        #     timeout=None,
        #     max_retries=2,
        #     gemini_api_key=os.getenv("GOOGLE_API_KEY")
        # )
        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.0,
            max_retries=2,
            timeout=30,
        )
    )
    history = await agent.run()
    result = history.final_result()
    print('------------------------')
    print(result)

#asyncio.run(main())