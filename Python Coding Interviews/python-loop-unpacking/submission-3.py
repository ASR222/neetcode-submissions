from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    Name = None
    best_score = -1
    for x, y in scores:
        if best_score == -1:
            best_score = y
            Name = x
        elif best_score < y:
            best_score = y
            Name = x
    return Name
        



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
