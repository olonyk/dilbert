from os.path import isfile
from os.path import join
from os.path import dirname
from os import system
from random import choice

class Actor:
    def __init__(self, base):
        self.base = base

    def act(self, action):
        """ Preformes the appropriate action as listed by the interpreter. This method is not
            cross-platform friendly due to the path handeling.
        """
        action = "../data" + action
        action = join(dirname(__file__), action)
        answer_list = self.base.read_file(action)
        answer = choice(answer_list)
        self.speak(answer)

        if "exit.dat" in action:
            return False
        return True

    def speak(self, answer):
        system("say '"+answer+"'")
