from typing import Dict, Optional, Tuple

def max_result_expression(expression:str, variables:Dict[str, Tuple[int, int]])->Optional[int]:
    print("hello")

if __name__ == '__main__':
    #os.environ['OUTPUT_PATH']
    f = open('inputfile/polishnotes.text', 'w')
    exp = str(input())
    variables = eval(input())
    res = max_result_expression(exp, vaiables)
    f.write(str(res) + "\n")