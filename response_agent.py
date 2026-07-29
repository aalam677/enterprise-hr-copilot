from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class ResponseAgent:

    def generate(
        self,
        query,
        context,
        tool_output
    ):

        # Leave Request

        if tool_output.get("tool") == "create_leave_request":

            req = tool_output.get(
                "data",
                {}
            )

            if "request_id" in req:

                return f"""
Leave Request Submitted

Request ID: {req.get('request_id')}

Status: {req.get('status')}
"""

            return f"""
Leave Request Failed

Details:
{req}
"""

        # Leave Balance

        if tool_output.get("tool") == "get_leave_balance":

            data = tool_output.get(
                "data",
                {}
            )

            if "annual" in data:

                return f"""
Your Current Leave Balance

Annual Leave : {data['annual']}
Casual Leave : {data['casual']}
Sick Leave   : {data['sick']}
"""

        # Holiday

        if tool_output.get("tool") == "holiday_calendar":

            return str(
                tool_output.get(
                    "data",
                    []
                )
            )

        # Employee

        if tool_output.get("tool") == "search_employee":

            return str(
                tool_output.get(
                    "data",
                    {}
                )
            )

        # RAG

        prompt = f"""
Question:
{query}

Context:
{context}

Tool Output:
{tool_output}

Answer the user.
"""

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content