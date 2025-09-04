from abc import ABC, abstractmethod
from helper import HeroDescription, Ngenter

print("--> Abstract Class And Decorator <--")
Ngenter()

class Button(ABC):

    def __init__(self, set_link):
      self.link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):

    def click(self):
        print(f"Go to : {self.link}")

    @Button.link.getter
    def link(self):
        return self.__link 

    @link.setter
    def link(self, input):
        self.link = input

         

btn = PushButton("https://chatgpt.com/")
btn.click()