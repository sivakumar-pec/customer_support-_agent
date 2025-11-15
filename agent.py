from scheduler_agent import SchedulerAgent
from resource_agent import ResourceAgent
from validator_agent import ValidatorAgent

class OrchestratorAgent:
    def __init__(self):
        self.scheduler = SchedulerAgent()
        self.resource = ResourceAgent()
        self.validator = ValidatorAgent()

    def handle_request(self, message):
        """Main controller for the whole multi-agent system."""
        
        if "schedule" in message.lower():
            return self.scheduler.create_schedule(message)

        elif "fetch" in message.lower() or "get" in message.lower():
            return self.resource.fetch_information(message)

        elif "validate" in message.lower():
            return self.validator.validate_text(message)

        else:
            return "I’m not sure which agent to use. Try: schedule, fetch, or validate."

if __name__ == "__main__":
    agent = OrchestratorAgent()
    print("Enterprise Agent Running...")
    
    while True:
        user_input = input("You: ")
        output = agent.handle_request(user_input)
        print("Agent:", output)
