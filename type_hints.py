from typing import List, Dict, NewType, Union, Optional

Grade = NewType("Grade", int)


class Student:
    def __init__(self, name: str, grades: List[Grade]) -> None:
        self.name = name
        self.grades = grades

    def cum_avg(self) -> float:
        return sum(self.grades) / len(self.grades)


# Here, `List[Union[int, str]]` means that the `lst` argument should be a list of integers and/or strings.
# `index: int` means that the `index` argument should be an integer.
# `Optional[Union[int, str]]` means that the function can return an integer, a string, or None.
def get_element_at_index(
    lst: List[Union[int, str]], index: int
) -> Optional[Union[int, str]]:
    if index < 0 or index >= len(lst):
        return None
    else:
        return lst[index]


def grade_point_averages(grades: Dict[str, List[int]]):
    avgs = {}
    for student, student_grades in grades.items():
        avgs[student] = sum(student_grades) / len(student_grades)
    return avgs


def greet(name: str) -> str:
    return f"Hello, {name}"


if __name__ == "__main__":
    print(greet("Rafi"))
    grades: Dict[str, List[int]] = {"Rafi": [2, 3, 4, 4], "WD": [4, 3, 4, 4]}
    print(grade_point_averages(grades))
