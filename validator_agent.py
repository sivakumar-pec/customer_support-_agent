"""
Validator Agent

This agent is responsible for:
- Checking data accuracy
- Validating reports or documents
- Ensuring required fields are filled
- Flagging missing or incorrect information
"""

class ValidatorAgent:
    def __init__(self):
        self.validation_rules = []

    def add_rule(self, rule_name, rule_function):
        """
        Add a custom validation rule.
        rule_function should return True/False.
        """
        self.validation_rules.append({"name": rule_name, "rule": rule_function})

    def validate(self, data):
        """
        Validate the provided data using all rules.
        Returns a list of errors (if any)
        """
        errors = []

        for rule in self.validation_rules:
            if not rule["rule"](data):
                errors.append(f"❌ Validation failed: {rule['name']}")

        if not errors:
            return ["✅ All validations passed."]
        return errors


# Example rules (optional to include)

def rule_not_empty(data):
    """Check if data is not empty."""
    return bool(data and len(data) > 0)

def rule_contains_required_field(data):
    """Check if data has a 'title' field."""
    return "title" in data

# Example usage
if __name__ == "__main__":
    validator = ValidatorAgent()
    validator.add_rule("Data should not be empty", rule_not_empty)
    validator.add_rule("Data must contain 'title'", rule_contains_required_field)

    sample_data = {"title": "Daily Report", "content": "All operations normal."}
    result = validator.validate(sample_data)
    print(result)

class ValidatorAgent:
    """
    This agent checks and validates user input or reports.
    """

    def validate_text(self, text):
        if not text or len(text.strip()) == 0:
            return False, "The input text is empty."

        if len(text) < 10:
            return False, "The input is too short to be valid."

        return True, "Validation passed: Text is valid."
