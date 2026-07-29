from mcp_client import (
    get_leave_balance,
    search_employee,
    get_holidays,
    create_leave_request
)


class HRToolAgent:

    def run(self, query):

        q = query.lower()

        if "apply" in q and "leave" in q:

            return {
                "tool": "create_leave_request",
                "data": create_leave_request(
                    {
                        "employee_id": "EMP001",
                        "from_date": "2025-08-12",
                        "to_date": "2025-08-14",
                        "leave_type": "Casual"
                    }
                )
            }

        if "balance" in q or "leave" in q:

            return {
                "tool": "get_leave_balance",
                "data": get_leave_balance("EMP001")
            }

        if "holiday" in q:

            return {
                "tool": "holiday_calendar",
                "data": get_holidays(2025)
            }

        if "employee" in q:

            return {
                "tool": "search_employee",
                "data": search_employee("John")
            }

        return {}