class Task:
    def __init__(self, text: str, options=[], win=False):
        self.text = text
        self.options = options
        self.win = win

    def addOption(self, task):
        self.options.append(task)

    def isWin(self):
        return self.win

    def getOptions(self):
        return self.options
    
    def display(self):
        print(self.text)
