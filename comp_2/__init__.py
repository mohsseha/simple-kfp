#WARNING: do not include any dependencies that would not work in a standard python3 installation 
#(this is because the kfp pipeline builder does not have access to the packages defined in this docker image)


def run(input1: float, random_str:str) -> float:
    # all imports should be here: 
    from typing import NamedTuple
    import os
    import comp_2.example as eg # this can't be "seen" by the pipeline code 

    print(f"running in comp_2, input1 was {input1} only works if I'm running in the clojure container")
    print(f"I'm doing nothing with the {random_str}")
    os.system('clj -e "(+ 1 1)"') # the clojure container has a python3 interperter installed 
    printf(f"calling a function with external dependencies {eg.ex_func()}")
    return input1