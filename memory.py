"""
Memory Module

This file manages short-term and long-term memory for the agents.
It includes:
- In-memory session storage
- Long-term memory bank
- Methods to save and retrieve memory
"""

class InMemorySessionService:
    def __init__(self):
        self.session_data = {}

    def set(self, key, value):
        """Store temporary session value."""
        self.session_data[key] = value

    def get(self, key, default=None):
        """Retrieve temporary session value."""
        return self.session_data.get(key, default)


class MemoryBank:
    def __init__(self):
        self.long_term_memory = []

    def save_memory(self, text):
        """Save memory into long-term storage."""
        self.long_term_memory.append(text)

    def search_memory(self, keyword):
        """Search memory that contains a keyword."""
        return [
            memory for memory in self.long_term_memory 
            if keyword.lower() in memory.lower()
        ]

