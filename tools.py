"""
Tools Module
These are utility tools that your agents can use.

Includes:
- Simple search tool (placeholder)
- Code execution simulation
- Data fetch simulation
"""

import time
import random


class SearchTool:
    """Simulated search tool (like Google Search)."""

    def search(self, query: str) -> str:
        print(f"[SearchTool] Searching for: {query}")
        time.sleep(1)  # simulate delay
        return f"Search results for '{query}' — (sample result)"


class CodeExecutionTool:
    """Simulated code execution tool."""

    def execute(self, code: str) -> str:
        print("[CodeExecution] Executing code...")
        time.sleep(1)

        try:
            local_vars = {}
            exec(code, {}, local_vars)
            return f"Execution successful. Output: {local_vars}"
        except Exception as e:
            return f"Execution failed: {e}"


class DataFetcherTool:
    """Simulated API fetch tool."""

    def fetch(self, url: str) -> str:
        print(f"[DataFetcher] Fetching from: {url}")
        time.sleep(1)

        fake_data = [
            "employee report data",
            "task list data",
            "resource usage data",
            "system logs data"
        ]

        return random.choice(fake_data)
        # tools.py
# Custom tools used by the Enterprise Workflow Automation Agent system

import time
import json

# -------------------------------
# TOOL 1 — Simulated Database Query
# -------------------------------
def fetch_from_database(query: str):
    # Simulated delay
    time.sleep(1)
    sample_data = {
        "employees": ["John", "Maya", "Kumar", "Sara"],
        "tasks": ["Prepare report", "Team meeting", "Client call"]
    }
    return sample_data.get(query, "No matching data found")


# -------------------------------
# TOOL 2 — Simulated Email Sender
# -------------------------------
def send_email(recipient: str, subject: str, message: str):
    time.sleep(1)
    return f"Email sent to {recipient} with subject '{subject}'."


# -------------------------------
# TOOL 3 — Simple JSON Validator
# -------------------------------
def validate_json_structure(json_string: str):
    try:
        data = json.loads(json_string)
        return "Valid JSON structure."
    except json.JSONDecodeError:
        return "Invalid JSON format."


# -------------------------------
# TOOL 4 — Basic Calculator
# -------------------------------
def calculate(expression: str):
    try:
        return eval(expression)
    except Exception:
        return "Invalid mathematical expression."


# -------------------------------
# TOOL REGISTRY
# -------------------------------
TOOLS = {
    "database_query": fetch_from_database,
    "send_email": send_email,
    "json_validator": validate_json_structure,
    "calculator": calculate
}

