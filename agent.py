from scheduler_agent import SchedulerAgent
from resource_agent import ResourceAgent
from validator_agent import ValidatorAgent
from memory import MemoryBank
from tools import Tools

class EnterpriseAgentOrchestrator:
    def __init__(self):
        self.memory = MemoryBank()
        self.tools = Tools()

        # Initialize sub-agents
        self.scheduler = SchedulerAgent(self.memory)
        self.resource_agent = ResourceAgent(self.tools, self.memory)
        self.validator = ValidatorAgent(self.memory)

    def handle_request(self, request: str):
        # Save request to memory
        self.memory.store("last_request", request)

        if "schedule" in request:
            return self.scheduler.create_schedule(request)

        elif "find" in request or "search" in request:
            return self.resource_agent.fetch_information(request)

        elif "validate" in request or "check" in request:
            return self.validator.validate_document(request)

        else:
            return "I can help with scheduling, information fetching, or validating documents."

if __name__ == "__main__":
    agent = EnterpriseAgentOrchestrator()

    print("Enterprise Workflow Automation AI Agent")
    print("Type 'exit' to stop.\n")

    while True:
        query = input("Ask the agent: ")

        if query.lower() == "exit":
            break

        response = agent.handle_request(query)
        print("Agent:", response)
