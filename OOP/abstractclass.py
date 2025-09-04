from helper import HeroDescription, Ngenter
from abc import ABC, abstractclassmethod

print("--> ABSTRACK CLASS <--")
Ngenter()

class Button(ABC):

    @abstractclassmethod
    def click(self):
        pass

class PushButton(Button):
    
    def click(self):
        print("Push button is clicked")

btn = PushButton()
btn.click()