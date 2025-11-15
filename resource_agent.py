"""
Resource Agent

This agent is responsible for:

• Fetching information
• Collecting data from tools
• Performing searches
• Acting as a helper agent for other agents
"""

import random
import time

class ResourceAgent:

    def search_data(self, query):
        """Simulate data searching."""
        sample_results = [
            "Report submitted successfully.",
            "Employee data verified.",
            "Task completed.",
            "Workflow updated.",
            "No errors found."
        ]
        time.sleep(1)  # simulate delay
        return f"Search result for '{query}': {random.choice(sample_results)}"

    def fetch_report(self):
        """Simulate fetching a report."""
        return {
            "title": "Daily Performance Report",
            "status": "Completed",
            "generated_at": "Today"
        }
