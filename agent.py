
from scheduler_agent import SchedulerAgent
from resource_agent import ResourceAgent
from validator_agent import ValidatorAgent
from memory import MemoryBank
from tools import get_current_time, simple_search

def main():
    print("\n===== ENTERPRISE WORKFLOW AUTOMATION AGENT =====\n")

    memory = MemoryBank()

    scheduler = SchedulerAgent()
    resource = ResourceAgent()
    validator = ValidatorAgent()

    # Example task
    task = "Prepare weekly enterprise report"
    print(f"Task Received: {task}")

    # Save to memory
    memory.store("last_task", task)

    # Step 1: Scheduling
    schedule = scheduler.create_schedule(task)
    print(f"Schedule Created: {schedule}")

    # Step 2: Get resource info
    resources = resource.fetch_resources(task)
    print(f"Resources Fetched: {resources}")

    # Step 3: Validate output
    is_valid = validator.validate(schedule)
    print(f"Validation: {is_valid}")

    # Step 4: Use Tool
    time = get_current_time()
    print(f"Current Time: {time}")

    # Step 5: Search using tool
    search_result = simple_search("Enterprise process automation")
    print(f"Search Result: {search_result}")

    print("\n===== TASK COMPLETED SUCCESSFULLY =====\n")

if __name__ == "__main__":
    main()
