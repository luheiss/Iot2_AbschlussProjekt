import random
import os
import json

"""
TODO
-Write a class that randomly chooses a question from json
-Add methods for the usage in QuestionModule
"""

class ReadJson():
    # Das aktuelle Arbeitsverzeichnis ermitteln
    currentDirectory = os.getcwd()
    print("Das aktuelle Verzeichnis ist:", currentDirectory)
    # Der Pfad zur JSON-Datei im aktuellen Verzeichnis
    jsonFilePath = os.path.join(currentDirectory, 'Questions.json')

    print(jsonFilePath)

    try:
        with open(jsonFilePath, 'r') as file:
            data = json.load(file)
            numsOfQuestions = len(data["Questions"].keys())
            print(f"{len(data["Questions"].keys())}")

    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
    except json.JSONDecodeError:
        print("Fehler beim Dekodieren der JSON-Datei.")
    except KeyError as e:
        print(f"Schlüssel {e} nicht in den Daten vorhanden.")
    
    def __init__(self):
        self.question = random.randint(1,self.numsOfQuestions)

    def get_question(self) -> str:
        return self.data["Questions"][str(self.question)]["question"]
    
    def get_answers(self):
        return self.data

    def get_question(cls):
        pass

    def get_question(cls):
        pass