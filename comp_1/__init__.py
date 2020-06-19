#WARNING: do not include any dependencies that would not work in a standard python3 installation 
#(this is because the kfp pipeline builder does not have access to the packages defined in this docker image)
from typing import NamedTuple
def run(input1: float,input2: float) -> NamedTuple('Cmp1Output', [('input1', float), ('input2', float), ('result', float)]):
    # if you need external deps they should be imported here: 
    
    print(f"running in comp_1, input1 was {input1} and inptu 2= {input2}")

    from collections import namedtuple
    comp_output = namedtuple('Cmp1Output', ['input1', 'input2', 'result'])
    return comp_output(input1, input2, input1*input2)
