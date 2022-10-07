import requests
from typing import List, Dict, Optional, Tuple
import parse
import time

kBase_url = "https://mipt1.ru/1_2_3_4_5_kor.php?sem={0}&zad={1}"
kFound_str = "Задача {0} найдена в Корявове на странице №{:d}!"

def test_one_problem(semester: int, problem: str) -> Optional[Tuple[str, int]]:
    url = kBase_url.format(semester, problem)
    resp = requests.get(url)
    text = resp.content.decode("cp1251")
    res = parse.search(kFound_str, text)
    if res is not None:
        return (res.fixed[0], res.fixed[1])
    return None



def test_list_of_problems(semester: int, problems: List[str]):
    found_problems: Dict[str, int] = {}
    not_found_problems: List[str] = []
    for problem in problems:
        ans = test_one_problem(semester, problem)
        if ans is not None:
            found_problems[ans[0]] = ans[1]
        else:
            not_found_problems.append(problem)
        # time.sleep(0.5)
    print("Not found:")
    print(", ".join(not_found_problems))
    print("Found:")
    for problem, page in found_problems.items():
        print(f"{problem} - page {page}")

def parse_problems(path: str):
    with open(path) as file:
        problems = [line.strip() for line in file]
    return problems


def __main__():
    # Exception support is not implemented yet
    print("Main started")
    path = input("Please enter the path to a file with problems\n")
    problems = parse_problems(path)
    semester = int(input("Please enter the book (1 for mechanics, 2 for thermodynamics and so on)\n"))
    test_list_of_problems(semester, problems)
    print("Done!")

if __name__ == "__main__":
    __main__()
