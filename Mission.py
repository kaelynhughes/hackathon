from Task import Task 
from Option import Option
class Mission:
    # def __init__(self, filename: str):
        # self.filename = filename

    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def runMission(self):
        if len(self.tasks) < 1:
            print("Mission incomplete!")
            return

        currentTask = self.tasks[0]
        while True:
            currentTask.display()
            if currentTask.isWin(): 
                return
            print()
            options = currentTask.getOptions()
            for i in range(len(options)):
                print(f"{i + 1}: ")
                options[i].display()

            chosen = False
            while not chosen:
                choice = input(">> ")
                print()
                try:
                    choiceInt = int(choice)
                    if choiceInt > 0 and choiceInt < len(options):
                        chosen = True
                        currentTask = options[choiceInt - 1].getTask()
                except ValueError:
                    print("Invalid response")





