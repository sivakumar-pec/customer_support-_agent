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
