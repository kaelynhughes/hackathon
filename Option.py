from Task import Task
class Option:
    def __init__(self, text: str, task=None):
        self.text: str = text
        self.task: Task | None = task

    def setTask(self, task: Task):
        self.task = task

    def getTask(self):
        return self.task

    def display(self):
        print(self.text)

