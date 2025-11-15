from scheduler_agent import SchedulerAgent
from resource_agent import ResourceAgent
from validator_agent import ValidatorAgent
from memory import MemoryBank


class OrchestratorAgent:
    """
    Main orchestrator that coordinates all sub-agents.
    """

    def __init__(self):
        self.memory = MemoryBank()
        self.scheduler = SchedulerAgent(self.memory)
        self.resource = ResourceAgent(self.memory)
        self.validator = ValidatorAgent(self.memory)

    def run(self, task):
        print("\n===== ENTERPRISE WORKFLOW AUTOMATION AGENT =====")

        # Step 1: Save user request to memory
        self.memory.save("latest_task", task)

        # Step 2: Routing logic
        if "schedule" in task.lower():
            return self.scheduler.handle(task)

        elif "fetch" in task.lower() or "get" in task.lower():
            return self.resource.handle(task)

        elif "check" in task.lower() or "validate" in task.lower():
            return self.validator.handle(task)

        else:
            return "I can only schedule tasks, fetch info, or validate documents at the moment."


if __name__ == "__main__":
    agent = OrchestratorAgent()
    while True:
        user_input = input("\nEnter your request: ")
        response = agent.run(user_input)
        print("\nAgent Response:", response)
