import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

task = """
   ### Prompt for Review us star rating directly automation

**Objective:**
Visit [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1), select star rating and see results.

**Important:**
- Make sure that you select "Star rating" .
- After selecting the star rating, a new form will appear and you should fill out the form.
---

### Step 1: Navigate to the Website 
- Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).

---

### Step 2: Select the Star Rating
- Wait for the star rating section to load.
- Select the **first star** (1-star rating).
- Click the **"Next"** button to proceed.

---

### Step 3: Fill Out the Feedback Form
- Wait for the feedback form to appear after clicking "Next".
- Enter the following dummy details:
  - **Review/Comment**: "Service was very slow and food was cold."
  - **Name**: "Jane Doe"
  - **Email**: "janedoe123@example.com"
- Check the box that says **"I would like to be contacted."**

---

### Step 4: Submit and Exit
- Click the **"Submit"** button on the form.
- Wait for the confirmation or success message.
- Close the browser window.

---


**Important:** Ensure efficiency and accuracy throughout the process."""

# task2 = """
# ### Prompt for Review Us Star Rating Automation

# **Objective:**
# Visit [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1), select a 1-star rating, fill out the review form, and submit it.

# **Important:**
# - Ensure you select the 1-star rating.
# - After selecting the star rating and clicking "Next", a feedback form should appear.
# - Fill out the form with dummy information and check the contact permission box.

# ---

# ### Step 1: Navigate to the Website
# - Open [birdeye review us](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1) in a browser.

# ---

# ### Step 2: Select the Star Rating
# - Wait for the star rating section to load.
# - Select the **first star** (1-star rating).
# - Click the **"Next"** button to proceed.

# ---

# ### Step 3: Fill Out the Feedback Form
# - Wait for the feedback form to appear after clicking "Next".
# - Enter the following dummy details:
#   - **Review/Comment**: "Service was very slow and food was cold."
#   - **Name**: "Jane Doe"
#   - **Email**: "janedoe123@example.com"
# - Check the box that says **"I would like to be contacted."**

# ---

# ### Step 4: Submit and Exit
# - Click the **"Submit"** button on the form.
# - Wait for the confirmation or success message.
# - Close the browser window.

# ---

# **Important:** Ensure each UI element is visible before interacting. Complete all steps without skipping.
# """

task1 = """
  ### Prompt: Submit a 1-Star Review on Birdeye

**Objective:**  
Visit the Birdeye review form for Dumpling Baby China Bistro and submit a 1-star review.

**Steps:**
1. Go to [this link](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).
2. Wait for the star rating section to load.
3. Select the **first star** to give a 1-star rating.
4. Click the **"Next"** button.
5. Wait for the feedback form to appear.
6. Fill out the form using:
   - **Review:** "Service was very slow and food was cold."
   - **Name:** "Jane Doe"
   - **Email:** "janedoe123@example.com"
   - Check the box: "I would like to be contacted."
7. Click **"Submit"**.
8. After submission:
   - **Do not click or interact with any link or modal related to Privacy Policy or Terms.**
   - **Do not accept any follow-up dialog or redirection.**
   - **If a popup/modal appears, dismiss or close it without interaction.**
   - **Do not click buttons like “Continue”, “Learn more”, or anything outside the success confirmation.**
9. Confirm the review was submitted and close the browser or exit.
"""

task2 = """
  ### Prompt: Submit a 2-Star Review on Birdeye

**Objective:**  
Visit the Birdeye review form for Dumpling Baby China Bistro and submit a 2-star review.

**Steps:**
1. Go to [this link](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).
2. Wait for the star rating section to load.
3. Select the **second star** to give a 2-star rating.
4. Click the **"Next"** button.
5. Wait for the feedback form to appear.
6. Fill out the form using:
   - **Review:** "Below average experience, not satisfied."
   - **Name:** "Jane Doe"
   - **Email:** "janedoe123@example.com"
   - Check the box: "I would like to be contacted."
7. Click **"Submit"**.
8. After submission:
   - **Do not click or interact with any link or modal related to Privacy Policy or Terms.**
   - **Do not accept any follow-up dialog or redirection.**
   - **If a popup/modal appears, dismiss or close it without interaction.**
   - **Do not click buttons like “Continue”, “Learn more”, or anything outside the success confirmation.**
9. Confirm the review was submitted and close the browser or exit.
"""

task3 = """
  ### Prompt: Submit a 3-Star Review on Birdeye

**Objective:**  
Visit the Birdeye review form for Dumpling Baby China Bistro and submit a 3-star review.

**Steps:**
1. Go to [this link](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).
2. Wait for the star rating section to load.
3. Select the **third star** to give a 3-star rating.
4. Click the **"Next"** button.
5. Wait for the feedback form to appear.
6. Fill out the form using:
   - **Review:** "It was okay, but could be better."
   - **Name:** "Jane Doe"
   - **Email:** "janedoe123@example.com"
   - Check the box: "I would like to be contacted."
7. Click **"Submit"**.
8. After submission:
   - **Do not click or interact with any link or modal related to Privacy Policy or Terms.**
   - **Do not accept any follow-up dialog or redirection.**
   - **If a popup/modal appears, dismiss or close it without interaction.**
   - **Do not click buttons like “Continue”, “Learn more”, or anything outside the success confirmation.**
9. Confirm the review was submitted and close the browser or exit.
"""

task4 = """
  ### Prompt: Submit a 4-Star Review on Birdeye

**Objective:**  
Visit the Birdeye review form for Dumpling Baby China Bistro and submit a 4-star review.

**Steps:**
1. Go to [this link](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).
2. Wait for the star rating section to load.
3. Select the **fourth star** to give a 4-star rating.
4. Click the **"Next"** button.
5. Wait for the feedback form to appear.
6. Fill out the form using:
   - **Review:** "Good service and food, minor issues."
   - **Name:** "Jane Doe"
   - **Email:** "janedoe123@example.com"
   - Check the box: "I would like to be contacted."
7. Click **"Submit"**.
8. After submission:
   - **Do not click or interact with any link or modal related to Privacy Policy or Terms.**
   - **Do not accept any follow-up dialog or redirection.**
   - **If a popup/modal appears, dismiss or close it without interaction.**
   - **Do not click buttons like “Continue”, “Learn more”, or anything outside the success confirmation.**
9. Confirm the review was submitted and close the browser or exit.
"""

task5 = """
  ### Prompt: Submit a 5-Star Review on Birdeye

**Objective:**  
Visit the Birdeye review form for Dumpling Baby China Bistro and submit a 5-star review.

**Steps:**
1. Go to [this link](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).
2. Wait for the star rating section to load.
3. Select the **fifth star** to give a 5-star rating.
4. Click the **"Next"** button.
5. Wait for the feedback form to appear.
6. Fill out the form using:
   - **Review:** "Excellent service and delicious food!"
   - **Name:** "Jane Doe"
   - **Email:** "janedoe123@example.com"
   - Check the box: "I would like to be contacted."
7. Click **"Submit"**.
8. After submission:
   - **Do not click or interact with any link or modal related to Privacy Policy or Terms.**
   - **Do not accept any follow-up dialog or redirection.**
   - **If a popup/modal appears, dismiss or close it without interaction.**
   - **Do not click buttons like “Continue”, “Learn more”, or anything outside the success confirmation.**
9. Confirm the review was submitted and close the browser or exit.
"""

def count_tokens(prompts: list[str]) -> int:
    model = genai.GenerativeModel("gemini-1.5-flash")
    total_tokens = 0
    for prompt in prompts:
        tokens = model.count_tokens(prompt).total_tokens
        total_tokens += tokens
    return total_tokens


async def main():
    
    tasks = [task1,task2,task3,task4,task5]
    print(f"🔢 Token count for task: {count_tokens(tasks)}\n")
    for task in tasks:
        agent = Agent(
            task=task,
            llm=ChatGoogleGenerativeAI(
                model="gemini-1.5-flash",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                gemini_api_key=os.getenv("GOOGLE_API_KEY")
            )
        )
        print(f"\nRunning agent for task:\n{'-'*40}\n{task.strip()[:100]}...")
        await agent.run()

asyncio.run(main())