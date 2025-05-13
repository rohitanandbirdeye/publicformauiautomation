install packages

Start the FastAPI server using Uvicorn:
uvicorn main:app --reload

Access the API documentation at:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

Use the endpoints to trigger tasks:
POST /run-dlc: Runs the DLC task.
POST /run-reviewus: Runs the Review Us task.
POST /run-all: Runs both tasks sequentially.