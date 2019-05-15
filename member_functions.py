import matplotlib.pyplot as plt
import numpy as np

# Grades cualification member function

def bad_grade(grade):
    if grade < 2:
        return float(1)
    if grade >= 2 and grade < 4:
        return float((-1/2)*grade + 2)
    if grade >= 4 and grade <= 5:
        return float(0)

def regular_grade(grade):
    if grade < 2:
        return float((1/2)*grade)
    if grade >= 2 and grade < 4:
        return float(1)
    if grade >= 4 and grade <= 5:
        return float(-1*grade + 5)

def good_grade(grade):
    if grade < 2:
        return float(0)
    if grade >= 2 and grade < 4:
        return float((1/2)*grade - 1)
    if grade >= 4 and grade <= 5:
        return float(1)


# Professor's opinion member function

def bad_opinion(opinion):
    if opinion < 30:
        return float(1)
    if opinion >= 30 and opinion < 70:
        return float((-1/40)*opinion + (7/4))
    if opinion >= 70 and opinion <= 100:
        return float(0)

def regular_opinion(opinion):
    if opinion < 30:
        return float((1/30)*opinion)
    if opinion >= 30 and opinion < 70:
        return float(1)
    if opinion >= 70 and opinion <= 100:
        return float((-1/30)*opinion + (10/3))

def good_opinion(opinion):
    if opinion < 30:
        return float(0)
    if opinion >= 30 and opinion < 70:
        return float((1/40)*opinion - (3/4))
    if opinion >= 70 and opinion <= 100:
        return float(1)


# opinions = np.arange(0,100,0.5)
# grades = np.arange(0,5,0.15)

# b_opinions = []
# r_opinions = []
# g_opinions = []
# for op in opinions:
#     b_opinions.append(bad_opinion(op))
#     r_opinions.append(regular_opinion(op))
#     g_opinions.append(good_opinion(op))

# b_grades = []
# r_grades = []
# g_grades = []
# for gr in grades:
#     b_grades.append(bad_grade(gr))
#     r_grades.append(regular_grade(gr))
#     g_grades.append(good_grade(gr))

# plt.plot(opinions, b_opinions, opinions, r_opinions, opinions, g_opinions)
# plt.plot(grades, b_grades, grades, r_grades, grades, g_grades)
# plt.show()
