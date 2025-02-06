import random

INTERVALLOWERBOUND = 5 #lower bound for random interval
INTERVALUPPERBOUND = 10 #upper bound for random interval

class RandomInterval():
    radomInterval = random.randint(INTERVALLOWERBOUND, INTERVALUPPERBOUND)
    gameCanStart = True

    @classmethod
    def get_random_interval(cls):
        print(f"Derzeitiges Interval: {cls.radomInterval}")
        return cls.radomInterval
    
    @classmethod
    def set_random_interval(cls):
        cls.radomInterval =  random.randint(INTERVALLOWERBOUND, INTERVALUPPERBOUND)
        print(f"Neues Intervall: {cls.radomInterval}")