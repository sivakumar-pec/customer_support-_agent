# validator_agent.py
# This agent checks and validates text, reports or task data

class ValidatorAgent:
    def __init__(self):
        self.name = "Validator Agent"

    def validate_text(self, text):
        """
        Simple validation rules:
        - Not empty
        - Must be at least 10 characters
        - Should not contain 'error', 'fail', 'fake'
        """
        if not text or len(text.strip()) == 0:
            return {
                "status": "Invalid",
                "reason": "Text is empty"
            }

        if len(text) < 10:
            return {
                "status": "Invalid",
                "reason": "Text is too short"
            }

        bad_words = ["error", "fail", "fake"]
        for word in bad_words:
            if word in text.lower():
                return {
                    "status": "Invalid",
                    "reason": f"Text contains restricted word: {word}"
                }

        return {
            "status": "Valid",
            "reason": "Text passed all validation checks"
        }


# Testing the agent directly (optional)
if __name__ == "__main__":
    agent = ValidatorAgent()
    test_text = "This report is correct and verified"
    print(agent.validate_text(test_text))
