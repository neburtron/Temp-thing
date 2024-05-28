import commands
import llm_interface
import sys
import os

class Main:
    def init(self, protagonist):
        self.array = []
        self.data_folder = "data"
        self.characters = "characters"
        self.protagonist = protagonist    

        self.character_path = os.path.join(self.data_folder, self.characters, self.protagonist)
        self.protagonist_raw = []
        self.town_raw = []

        self.protagonist_cooked = ""
        self.town_cooked = ""

        self.instruct1 = commands.read("Prompts/decide_next")

        self.start()

    def start(self):
        self.array.clear()

        # Refresh Data
        self.protagonist_raw = commands.load(self.character_path)
        self.town_raw = commands.load(os.path.join(self.data_folder, "town.json"))

        # Condense info into good format
        # This is gonna change when I figure out the API stuff. 
        
        self.protagonist_cooked = ("Character: testing")
        self.town_cooked = ("Town: testing")

        self.array.append({"role": "system", "content": self.instruct1})
        self.array.append({"role": "user", "content": self.protagonist_cooked})
        self.array.append({"role": "user", "content": self.town_cooked})
        # Test to see which is better, user giving town + protagonist cooked, user or system. 
        
        thing = llm_interface.main(self.array)
        print(thing)
        #commands.write("testing.txt", thing)

        """
        process from here on
        1. Get protagonist's next steps
        2. determine odds of that
        3. get outcome of that 
            - now in this thing's commands.py
            - Not percentage chances, rolls dice with X sides
        4. interpret - bigger thing
        """
        return

if __name__ == "__main__":
    instance = Main()
    instance.init("protagonist.json")