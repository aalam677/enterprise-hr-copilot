import requests

BASE_URL = "http://localhost:8001"


def get_leave_balance(employee_id):

    try:

        response = requests.get(
            f"{BASE_URL}/leave_balance/{employee_id}"
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


def search_employee(name):

    try:

        response = requests.get(
            f"{BASE_URL}/employee/{name}"
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


def get_holidays(year):

    try:

        response = requests.get(
            f"{BASE_URL}/holiday/{year}"
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


def create_leave_request(payload):

    try:

        response = requests.post(
            f"{BASE_URL}/leave_request",
            json=payload
        )

        print("\n========== MCP DEBUG ==========")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        print("================================\n")

        response.raise_for_status()

        if not response.text.strip():

            return {
                "error": "Empty response from MCP Server"
            }

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }