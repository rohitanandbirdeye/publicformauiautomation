import asyncio
import dlc
import reviewus_rate
from fastapi import FastAPI
import os
import glob
import json
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    'null'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/getAutomationResult")
def getAutomationResult():
    directory = "outputs"
    files = glob.glob(f"{directory}/result_*.json")
    if not files:
        return {"error": "No result files found"}
    
    latest_file = max(files, key=os.path.getctime)
    with open(latest_file, "r") as file:
        data = json.load(file)

    return {"final_result": data}

@app.get("/testpublicformulrs")
async def testpublicformulrs():
    start_timestamp = time.time()
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

    end_timestamp = time.time()
    final_result = {
        "start":start_timestamp,
        "end": end_timestamp,
        "pages": {
            "DLC": {
                "success": dlc_history.is_successful(),
                "message": dlc_history.final_result(),
            }, 
            "Review us": {
                "success": reviewusrate_history.is_successful(),
                "message": reviewusrate_history.final_result()
            },
        }
    }

    # final_result = {
    #     "start":start_timestamp,
    #     "end": end_timestamp,
    #     "pages": {
    #         "DLC Page": {
    #             "success": True,
    #             "message": "DLC Page is working as expected/....",
    #         }, 
    #         "Review us Page": {
    #             "success": True,
    #             "message": "Review Us Page is working as expected/...",
    #         },
    #     }
    # }
    final_result_obj = json.dumps(final_result, indent=4)
    
    print(f"Timestamp: {end_timestamp}")
    filename = f"outputs/result_{end_timestamp}.json"  # Add string to timestamp
    with open(filename, "w") as outfile:
        outfile.write(final_result_obj)

    return {"final_result": final_result}

# if __name__ == "__main__":
#     asyncio.run(run_all())