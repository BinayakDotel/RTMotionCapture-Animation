from email.mime.text import MIMEText

class Greeter():
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hi "+self.name+", You did it!"