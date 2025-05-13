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

@app.get("/testpublicformulrs")
async def testpublicformulrs():
    print("Running All Tasks...")
    print("Running DLC Task...")
    dlc_history = await dlc.main()
    print("\nDLC Task Completed.\n")
    print("------------------------\n")
    print("Running Review Us Task...")
    reviewusrate_history = await reviewus_rate.main()
    print("\nReview Us Task Completed.\n")
    print("------------------------\n")
    print("All Tasks Completed.\n")
    return {
        "DLC Page Success": dlc_history.is_successful(), 
        "DLC Page Final Result": dlc_history.final_result(),
        "Review Us Page Success": reviewusrate_history.is_successful(),
        "Review Us Page Final Result": reviewusrate_history.final_result()
    }

# if __name__ == "__main__":
#     asyncio.run(run_all())