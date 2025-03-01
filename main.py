from Task import Task
from Option import Option
from Mission import Mission
def main():
    defaultTasks = createTasks()
    runGame(defaultTasks)

def runGame(tasks: list[Task]):
    mission = Mission(tasks)
    mission.runMission()


def createTasks() -> list[Task]:
    tasks: list[Task] = []

    task1 = Task(
        "You wake up in a room. You look around and decide to examine the...",
            )
    returnToStart = Option("Start over...", task1)
    death = Task("Death!", [returnToStart])
    tasks.append(task1)

    keepLooking = Option("Keep looking.", task1)
    open = Option("Open it.", death)
    openWin = Option("Open it.", Task("You win!", [], True))

    task2 = Task("You see a blue door.", [keepLooking, open])
    tasks.append(task2)

    task3 = Task("You see a red door.", [keepLooking, open])
    tasks.append(task3)

    task4 = Task("You see a yellow door.", [keepLooking, openWin])
    tasks.append(task4)

    option1 = Option("Right wall.", task2)
    option2 = Option("Left wall.", task3)
    option3 = Option("Front wall.", task4)

    task1.addOption(option1)
    task1.addOption(option2)
    task1.addOption(option3)

    return tasks

main()
