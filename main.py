from fastapi import FastAPI
from models import Target
from scanner import run_scan, save_results
from validator import validate_results

app = FastAPI(title="AI Kill Chain Monitor")

@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/scan")
def scan_target(data: Target):
    # Phase 2: Scanning
    scan_result = run_scan(data.target)

    # Phase 3: Validation
    validated = validate_results(scan_result)

    # Save results
    save_results(validated)

    return validated
