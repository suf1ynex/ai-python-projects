
class AIAgent:
    # Class variable
    total_agents = 0

    def __init__(self, name, role, model):
        # Instance variables
        self.name = name
        self.role = role
        self.model = model
        self.history = []
        self.tasks_completed = 0

        # Increment total number of agents
        AIAgent.total_agents += 1

    def process_task(self, task):
        self.history.append(task)
        self.tasks_completed += 1
        return f"{self.name} ({self.role}) processed: {task}"

    def get_report(self):
        last_task = self.history[-1] if self.history else "None"

        return (
            "=== Agent Report ===\n"
            f"Name: {self.name}\n"
            f"Role: {self.role}\n"
            f"Model: {self.model}\n"
            f"Tasks completed: {self.tasks_completed}\n"
            f"Last task: {last_task}"
        )

    def __str__(self):
        return f"AIAgent({self.name} | {self.role} | {self.model})"


# Test the AI Agent Simulator
researcher = AIAgent("ResearchBot", "Researcher", "gpt-4")
writer = AIAgent("WriterBot", "Writer", "gpt-3.5")

print(researcher.process_task("Analyse competitor landscape"))
print(researcher.process_task("Identify top 5 AI trends"))
print(writer.process_task("Write executive summary"))

print()
print(researcher.get_report())
print()
print(writer.get_report())
print()
print(f"Total agents created: {AIAgent.total_agents}")
