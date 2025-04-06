from fastapi import FastAPI

app = FastAPI()

scam_database = {
    "1234567890": {"scam": True, "alert": "Potential Scam"},
    "0987654321": {"scam": True, "alert": "Potential Scam"}
}

@app.get("/api/verify-number")
async def verify_number(phone: str):
    record = scam_database.get(phone, {"scam": False, "alert": "Clear"})
    return record

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)