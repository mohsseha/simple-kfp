from typing import NamedTuple
import os

def run(input1: float) -> float:
    print(f"running in comp_2, input1 was {input1} only works if I'm running in the clojure container")

    os.system('clj -e "(+ 1 1)"') # the clojure container has a python3 interperter installed 
    return input1 
