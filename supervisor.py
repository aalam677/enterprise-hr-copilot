from retrieval_agent import RetrievalAgent
from hr_tool_agent import HRToolAgent
from response_agent import ResponseAgent


class Supervisor:

    def __init__(self):

        self.rag = RetrievalAgent()
        self.tool = HRToolAgent()
        self.response = ResponseAgent()

    def run(self, query):

        agent_flow = [
            "Supervisor Agent"
        ]

        context = ""
        sources = []
        tool_result = {}

        q = query.lower()

        if any(
            word in q
            for word in [
                "policy",
                "maternity",
                "work from home",
                "notice period"
            ]
        ):

            retrieval = self.rag.run(query)

            context = "\n".join(
                retrieval["context"]
            )

            sources = retrieval[
                "sources"
            ]

            agent_flow.append(
                "Policy Retrieval Agent"
            )

        if any(
            word in q
            for word in [
                "leave",
                "balance",
                "holiday",
                "employee",
                "apply"
            ]
        ):

            tool_result = self.tool.run(
                query
            )

            agent_flow.append(
                "HR Tool Agent"
            )

        agent_flow.append(
            "Response Agent"
        )

        answer = self.response.generate(
            query=query,
            context=context,
            tool_output=tool_result
        )

        return {
            "answer": answer,
            "agent_flow": agent_flow,
            "sources": sources,
            "tool_calls": [
                tool_result
            ] if tool_result else []
        }
