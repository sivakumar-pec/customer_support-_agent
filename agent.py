from scheduler_agent import SchedulerAgent
from resource_agent import ResourceAgent
from validator_agent import ValidatorAgent
from memory import MemoryBank
from tools import log_task


class OrchestratorAgent:

    def __init__(self):
        self.scheduler = SchedulerAgent()
        self.resource = ResourceAgent()
        self.validator = ValidatorAgent()
        self.memory = MemoryBank()

    def run(self):
        print("\n--- Enterprise AI Agent Started ---")

        task = input("Enter your task: ")

        valid, message = self.validator.validate_text(task)
        print("Validator:", message)

        if not valid:
            return

        self.memory.store(task)
        print("Memory: Task stored")

        time = self.scheduler.schedule_task(task)
        print(f"Scheduler: Task scheduled at {time}")

        resource = self.resource.get_resource(task)
        print("Resource Agent:", resource)

        log = log_task(task)
        print("Tool:", log)

        print("\n Task Successfully Processed by Multi-Agent System")


if __name__ == "__main__":

