from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_student = None
    best_score = -1
    for i, j in scores:
        if best_score == -1:
            best_score = j
            best_student = i
        elif j > best_score:
            best_score = j
            best_student = i
    
    return best_student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
