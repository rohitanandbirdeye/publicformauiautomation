import asyncio
from fastapi import FastAPI
import os
import glob
import json
import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from publicFormScripts import checkin, dlc, reviewus_rate

app = FastAPI()

# Serve static files (main.html, script.js, etc.)
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

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

@app.get("/", include_in_schema=False)
def root():
    return FileResponse(os.path.join(static_dir, "main.html"))

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

@app.post("/run-checkin")
async def run_checkin():
    print("Running Checkin Task...")
    await checkin.main()
    return {"status": "Checkin Task Completed"}

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
    print("Running Checkin Task...")
    checkin_history = await checkin.main()
    print("\nCheckin Task Completed.\n")
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
            "Review us rating": {
                "success": reviewusrate_history.is_successful(),
                "message": reviewusrate_history.final_result()
            },
            "Checkin": {
                "success": checkin_history.is_successful(),
                "message": checkin_history.final_result()
            }
        }
    }

    final_result_obj = json.dumps(final_result, indent=4)
    
    print(f"Timestamp: {end_timestamp}")
    filename = f"outputs/result_{end_timestamp}.json"  # Add string to timestamp
    with open(filename, "w") as outfile:
        outfile.write(final_result_obj)

    return {"final_result": final_result}

# if __name__ == "__main__":
#     asyncio.run(run_all())