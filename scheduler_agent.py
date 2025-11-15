"""
Scheduler Agent
----------------
This agent is responsible for:
- Scheduling tasks
- Managing deadlines
- Creating reminders
- Coordinating workflow timelines
"""

from datetime import datetime, timedelta

class SchedulerAgent:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, due_in_hours):
        """Add a new task with a deadline."""
        due_time = datetime.now() + timedelta(hours=due_in_hours)
        task = {
            "task": task_name,
            "due": due_time
        }
        self.tasks.append(task)
        return f"Task '{task_name}' scheduled. Due by {due_time.strftime('%Y-%m-%d %H:%M:%S')}"

    def list_tasks(self):
        """List all scheduled tasks."""
        if not self.tasks:
            return "No tasks scheduled."
        
        output = "Scheduled Tasks:\n"
        for t in self.tasks:
            output += f"- {t['task']} (Due: {t['due'].strftime('%Y-%m-%d %H:%M:%S')})\n"
        return output

    def remove_task(self, task_name):
        """Remove a specific task."""
        for t in self.tasks:
            if t['task'].lower() == task_name.lower():
                self.tasks.remove(t)
                return f"Task '{task_name}' removed."
        return f"No task found with the name '{task_name}'."
