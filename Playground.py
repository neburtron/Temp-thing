import commands
import llm_interface
import sys
import os

class main():
    
    def init(self, protagonist):
        
        self.array = []
        
        self.data_folder = "data"
        self.characters = "characters"
        self.protagonist = protagonist        
        
        self.character_path = os.join(self.data_folder,self.characters,self.protagonist)
        self.protagonist_raw = []
        self.town_raw = []
        
        
        self.start
        
        
    def start(self):
        self.array.clear
        
        # Refresh Data
        self.protagonist_raw = commands.load(self.character_path)
        self.town_raw = commands.load(os.join(self.data_folder, "town.json"))
        
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
    instance = main("protagonist.json")
    
    
# self.array.clear
# self.array.append({"role": thing, "content": message})
