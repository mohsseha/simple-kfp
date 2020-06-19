from typing import NamedTuple
import os

def run(input1: float, random_str:str) -> float:
    print(f"running in comp_2, input1 was {input1} only works if I'm running in the clojure container")
    print(f"I'm doing nothing with the {random_str}")
    os.system('clj -e "(+ 1 1)"') # the clojure container has a python3 interperter installed 
    return input1 
