from fastapi import FastAPI
import json
import uuid
import os

app = FastAPI()

# --------------------------------------
# Load Employee Data
# --------------------------------------

with open("employee_data.json", "r") as f:
    employees = json.load(f)

# --------------------------------------
# Load Holiday Data
# --------------------------------------

with open("holidays.json", "r") as f:
    holidays = json.load(f)

# --------------------------------------
# Create leave_requests.json if missing
# --------------------------------------

if not os.path.exists("leave_requests.json"):

    with open("leave_requests.json", "w") as f:
        json.dump([], f, indent=4)


# ======================================
# Leave Balance
# ======================================

@app.get("/leave_balance/{employee_id}")
def get_leave_balance(employee_id: str):

    employee = employees.get(employee_id)

    if not employee:
        return {
            "error": "Employee not found"
        }

    return {
        "annual": employee["annual_leave"],
        "casual": employee["casual_leave"],
        "sick": employee["sick_leave"]
    }


# ======================================
# Employee Search
# ======================================

@app.get("/employee/{name}")
def search_employee(name: str):

    for emp in employees.values():

        if name.lower() in emp["name"].lower():

            return emp

    return {
        "message": "Employee not found"
    }


# ======================================
# Holiday Calendar
# ======================================

@app.get("/holiday/{year}")
def holiday_calendar(year: int):

    return holidays.get(
        str(year),
        []
    )


# ======================================
# Create Leave Request
# ======================================

@app.post("/leave_request")
def create_leave_request(payload: dict):

    request_id = f"REQ-{uuid.uuid4().hex[:8].upper()}"

    leave_record = {
        "request_id": request_id,
        "employee_id": payload.get("employee_id"),
        "from_date": payload.get("from_date"),
        "to_date": payload.get("to_date"),
        "leave_type": payload.get("leave_type"),
        "status": "Submitted"
    }

    with open("leave_requests.json", "r") as f:
        requests_data = json.load(f)

    requests_data.append(leave_record)

    with open("leave_requests.json", "w") as f:
        json.dump(
            requests_data,
            f,
            indent=4
        )

    return {
        "request_id": request_id,
        "status": "Submitted"
    }


# ======================================
# Get All Leave Requests
# ======================================

@app.get("/leave_requests")
def get_leave_requests():

    with open(
        "leave_requests.json",
        "r"
    ) as f:

        return json.load(f)


# ======================================
# Health Check
# ======================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }