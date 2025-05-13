import asyncio
import dlc
import reviewus_rate
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Automation API"}

@app.post("/run-dlc")
async def run_dlc():
    print("Running DLC Task...")
    await dlc.main()
    return {"status": "DLC Task Completed"}

@app.post("/run-reviewus")
async def run_reviewus():
    print("Running Review Us Task...")
    await reviewus_rate.main()
    return {"status": "Review Us Task Completed"}

@app.post("/run-all")
async def run_all():
    print("Running All Tasks...")
    print("Running DLC Task...")
    dlc_history = await dlc.main()
    print("\nDLC Task Completed.\n")
    print("------------------------")
    print(f"Success: {dlc_history.is_successful()}")
    print(f"Final Result: {dlc_history.final_result()}")
    print("------------------------\n")
    await reviewus_rate.main()
    return {"status": "All Tasks Completed"}

# if __name__ == "__main__":
#     asyncio.run(run_all())