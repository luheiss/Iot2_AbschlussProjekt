"""This is a statemachine for the interface"""

#default state - window with title and button ready 
#state 1 - showing blue circles representing filled cups
#state 2 - a cup is removed - cricle changes color from red to blue and stays so
#state 3 - a random timed event - questions and minigames pop up, after finishing, set back to default


class InterfaceStates():
    #this is a prototype mockup - so some pseudo code is used here
    def __init__(self):
        self.state = "MainInterface"
    
    def show_state(self, state : int):
        
        if state == 2:
            print("state 2")
        elif state == 3:
            print("state 3")
        else:
            raise ValueError("Diesen State gibt es nicht")

        