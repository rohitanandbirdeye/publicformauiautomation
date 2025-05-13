import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from langchain_openai import ChatOpenAI

load_dotenv()

task1 = """
### Prompt: Submit a 1-Star Review on Birdeye

**Objective:**  
Visit the Birdeye review form for Dumpling Baby China Bistro and submit a 1-star review.

**Steps:**
1. Go to [this link](https://birdeye.com/dumpling-baby-china-bistro-165406729056862/review-us?dashboard=1&write=1).
2. Wait for the star rating section to load.
3. Select the **first star**.
4. Click the **"Next"** button.
5. Wait for the feedback form to appear.
6. Type into the **Experience** textarea: "The service was extremely slow, and the food arrived cold and tasteless."
7. Type into the **Name** field: "Tushar Aggarwal"
8. Type into the **Email** field: "tushar.aggarwal@birdeye.com"
9. Click outside the form to trigger events.
10. After filling all fields, **click outside the form or press Tab to trigger validation events**.
11. Wait and check if the **Submit button is enabled** (check until 15 seconds max).
12. If enabled, click **Submit**.
13. If the button does not enable after 15 seconds, **fail and exit**.
14. Confirm submission by looking for a confirmation message.
15. Close the browser.

```javascript
function forceFillInput(selector, value) {
    const el = document.querySelector(selector);
    if (el) {
        el.focus();
        el.value = value;
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
        el.blur();
    }
}
forceFillInput('textarea', 'The service was extremely slow, and the food arrived cold and tasteless.');
forceFillInput('input[name="name"]', 'Tushar Aggarwal');
forceFillInput('input[name="email"]', 'tushar.aggarwal@birdeye.com');
"""


async def main():
    agent = Agent(
        task=task1,
        llm=ChatOpenAI(
            model="gpt-4o",
            temperature=0,
            timeout=30,  # ✅ Always provide timeout to LLM calls (30 seconds safe default)
            max_retries=2,
            max_tokens=2048
        )  # ✅ Optional if your Agent supports it
    )
    try:
        await asyncio.wait_for(agent.run(), timeout=90)  # ✅ Overall agent timeout safety
    except asyncio.TimeoutError:
        print("❌ Agent task timed out after 90 seconds. Exiting gracefully.")

asyncio.run(main())