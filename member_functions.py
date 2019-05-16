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

# Chance of Aprobal member function 

def very_bad_chance(chance):
    if chance < 16:
        return float(1)
    if chance >= 16 and chance < 36:
        return float((-1/20)*chance + (36/20))
    if chance >= 36 and chance <= 100:
        return float(0)
def bad_chance(chance):
    if chance < 38:
        return float(1)
    if chance >= 38 and chance < 55:
        return float((-1/17)*chance + (55/17))
    if chance >= 55 and chance <= 100:
        return float(0)
def regular_chance(chance):
    if chance < 23:
        return float(0)
    if chance >= 23 and chance < 45:
        return float((1/22)*chance - (23/22))
    if chance >= 45 and chance <= 55:
        return float(1)
    if chance >= 55 and chance <= 77:
        return float((-1/22)*chance + (77/22))
    if chance >= 77 and chance <= 100:
        return float(0)
def good_chance(chance):
    if chance < 40:
        return float(0)
    if chance >= 40 and chance < 60:
        return float((1/20)*chance - 2)
    if chance >= 60 and chance <= 100:
        return float(1)
def very_good_chance(chance):
    if chance < 60:
        return float(0)
    if chance >= 60 and chance < 80:
        return float((1/20)*chance - 3)
    if chance >= 80 and chance <= 100:
        return float(1)

def eval_chances_func(chance):
    return (very_good_chance(chance),
            good_chance(chance),
            regular_chance(chance),
            bad_chance(chance),
            very_bad_chance(chance))

# fuzzify methods

def fuzzify_grades(raw_grades:list)->list:
    results = []
    for gr in raw_grades:
        results += [fuzzify_grade(gr)]
    return results
def fuzzify_opinions(raw_opinions:list)->list:
    results = []
    for op in raw_opinions:
        results += [fuzzify_opinion(op)]
    return results

def fuzzify_grade(grade):
    return {"bad":bad_grade(grade),"regular":regular_grade(grade),"good":good_grade(grade)}
def fuzzify_opinion(opinion):
    return {"bad":bad_opinion(opinion),"regular":regular_opinion(opinion),"good":good_opinion(opinion)}



# chances = np.arange(0,100,0.5)
# grades = np.arange(0,5,0.15)

# vb_chances = []
# b_chances = []
# r_chances = []
# g_chances = []
# vg_chances = []
# for op in chances:
#     vb_chances.append(very_bad_chance(op))
#     b_chances.append(bad_chance(op))
#     r_chances.append(regular_chance(op))
#     g_chances.append(good_chance(op))
#     vg_chances.append(very_good_chance(op))

# b_grades = []
# r_grades = []
# g_grades = []
# for gr in grades:
#     b_grades.append(bad_grade(gr))
#     r_grades.append(regular_grade(gr))
#     g_grades.append(good_grade(gr))

# plt.plot(chances, vb_chances, chances, b_chances, chances, r_chances, chances, g_chances, chances, vg_chances)
# plt.plot(grades, b_grades, grades, r_grades, grades, g_grades)
# plt.show()
