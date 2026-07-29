import streamlit as st
import requests
import time

API_URL = "http://localhost:8000"

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Enterprise HR Copilot",
    page_icon="🏢",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent_flow" not in st.session_state:
    st.session_state.agent_flow = []

if "tool_calls" not in st.session_state:
    st.session_state.tool_calls = []

if "sources" not in st.session_state:
    st.session_state.sources = []

# =====================================================
# HEADER
# =====================================================

st.title("🏢 Enterprise HR Copilot")
st.caption(
    "Multi-Agent Architecture + MCP + ChromaDB + RAG"
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("📄 HR Policy Upload")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file:

        if st.button("Upload PDF"):

            try:

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        "application/pdf"
                    )
                }

                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

                if response.status_code == 200:

                    st.success(
                        "PDF Uploaded Successfully"
                    )

                else:

                    st.error(
                        "Upload Failed"
                    )

            except Exception as e:

                st.error(str(e))

    st.divider()

    if st.button("Clear Session"):

        st.session_state.messages = []
        st.session_state.agent_flow = []
        st.session_state.tool_calls = []
        st.session_state.sources = []

        st.rerun()

    st.divider()

    st.subheader("Agent Execution Flow")

    if st.session_state.agent_flow:

        for step in st.session_state.agent_flow:

            st.success(step)

    else:

        st.info("No execution yet")

    st.divider()

    st.subheader("MCP Tool Calls")

    if st.session_state.tool_calls:

        for tool in st.session_state.tool_calls:

            st.json(tool)

    else:

        st.info("No tool calls")

# =====================================================
# DISPLAY CHAT HISTORY
# =====================================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# =====================================================
# CHAT INPUT
# =====================================================

prompt = st.chat_input(
    "Ask HR related questions..."
)

# =====================================================
# PROCESS QUERY
# =====================================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    start_time = time.time()

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        try:

            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "message": prompt
                }
            )

            result = response.json()

            answer = result.get(
                "answer",
                "No Answer Generated"
            )

            st.session_state.agent_flow = (
                result.get(
                    "agent_flow",
                    []
                )
            )

            st.session_state.tool_calls = (
                result.get(
                    "tool_calls",
                    []
                )
            )

            st.session_state.sources = (
                result.get(
                    "sources",
                    []
                )
            )

            response_placeholder.markdown(
                answer
            )

        except Exception as e:

            answer = f"Error: {str(e)}"

            response_placeholder.error(
                answer
            )

    elapsed = time.time() - start_time

    st.info(
        f"Response Time: {elapsed:.2f} sec"
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# =====================================================
# SOURCES
# =====================================================

st.divider()

st.subheader("Sources")

if st.session_state.sources:

    if isinstance(
        st.session_state.sources,
        list
    ):

        for source in st.session_state.sources:

            st.json(source)

    else:

        st.json(
            st.session_state.sources
        )

else:

    st.info(
        "No sources available"
    )

# =====================================================
# MCP TOOL OUTPUTS
# =====================================================

st.divider()

st.subheader("Tool Results")

if st.session_state.tool_calls:

    for call in st.session_state.tool_calls:

        st.json(call)

else:

    st.info(
        "No tool outputs"
    )

# =====================================================
# ARCHITECTURE VIEW
# =====================================================

st.divider()

st.subheader(
    "Multi-Agent Architecture"
)

st.code(
"""
User
 │
 ▼
Supervisor Agent
 │
 ├────▶ Retrieval Agent
 │          │
 │          ▼
 │      ChromaDB
 │
 ├────▶ HR Tool Agent
 │          │
 │          ▼
 │      MCP Server
 │
 ▼
Response Agent
 │
 ▼
Final Answer
"""
)