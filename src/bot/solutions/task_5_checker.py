from math import gcd
from random import randint
from subprocess import Popen, PIPE

def run(filepath: str, a: int, b: int) -> str:
    p = Popen(['python3', filepath], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
    stdout_data = p.communicate(f"{a} {b}")[0]
    p.terminate()
    return stdout_data.strip()

def check_task_5_solution(filepath) -> False:
    tests_count = 50
    correct_cnt = 0
    for i in range(tests_count):
        a = randint(1, 1000)
        b = randint(1, 1000)
        if run(filepath, a, b) == str(gcd(a, b)):
            correct_cnt += 1
    return correct_cnt, tests_count
