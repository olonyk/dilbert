
from objects import SpeechListener
from objects import Base
from objects import Interpreter
from objects import Actor

class Dilbert:
    def __init__(self):
        self.base = Base()
        self.listener = SpeechListener(self.base)
        self.interpreter = Interpreter(self.base)
        self.actor = Actor(self.base)

    def run(self):
        interview = True
        while interview:
            msg = self.listener.listen()
            action = self.interpreter.interpret(msg)
            interview = self.actor.act(action)


D = Dilbert()
D.run()