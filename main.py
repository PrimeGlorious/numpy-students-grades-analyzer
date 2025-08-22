import numpy as np

# The grade range is (1..10)
grades = np.array([
    [2, 3, 6, 10, 1],
    [1, 3, 5, 7, 2],
    [2, 4, 6, 8, 3],
    [3, 5, 7, 9, 4],
    [4, 6, 8, 10, 5],
    [9, 10, 10, 10, 6],
    [1, 5, 8, 10, 6],
    [2, 6, 9, 10, 7],
    [9, 10, 9, 10, 10],
])


class GradeChecker:
    def __init__(self, students):
        self.students = students

    def get_grades_stats(self) -> np.ndarray:
        max_grades = np.max(self.students, axis=1)
        min_grades = np.min(self.students, axis=1)
        mean_grades = np.mean(self.students, axis=1)
        return np.vstack([max_grades, min_grades, mean_grades]).T

    def get_best_students(self) -> np.ndarray:
        mean_grades = np.mean(self.students, axis=1)
        return self.students[mean_grades >= 8]


if __name__ == "__main__":
    class1 = GradeChecker(grades)
    class1_grades_stats = class1.get_grades_stats()
    print("Stats (max, min, mean):\n", class1_grades_stats)

    best_students_list = class1.get_best_students()
    print("Best students:\n", best_students_list)
