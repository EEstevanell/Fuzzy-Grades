import scipy.integrate as integrate
import member_functions as mf
import numpy as np

def run_defuzzyfiers( agregation_func):
    x = get_left_max(agregation_func)
    vg, g, r, b, vb  = mf.eval_chances_func(x)
    print("using left-most max value:\n\
            x = %s\n\
            f(x) = {very good aproval chance = %s,\n\
                    good aproval chance = %s,\n\
                    regular aproval chance = %s,\n\
                    bad aproval chance = %s,\n\
                    very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))

    x = get_right_max(agregation_func)
    vg, g, r, b, vb  = mf.eval_chances_func(x)
    print("using right-most max value:\n\
            x = %s\n\
            f(x) = {very good aproval chance = %s,\n\
                    good aproval chance = %s,\n\
                    regular aproval chance = %s,\n\
                    bad aproval chance = %s,\n\
                    very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))

    x = get_median_max(agregation_func)
    vg, g, r, b, vb  = mf.eval_chances_func(x)
    print("using median max value:\n\
            x = %s\n\
            f(x) = {very good aproval chance = %s,\n\
                    good aproval chance = %s,\n\
                    regular aproval chance = %s,\n\
                    bad aproval chance = %s,\n\
                    very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))
    
    x = centroid_method(agregation_func)
    vg, g, r, b, vb  = mf.eval_chances_func(x)
    print("using centroid method value:\n\
            x = %s\n\
            f(x) = {very good aproval chance = %s,\n\
                    good aproval chance = %s,\n\
                    regular aproval chance = %s,\n\
                    bad aproval chance = %s,\n\
                    very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))
    
    x = bisector_method(agregation_func)
    vg, g, r, b, vb  = mf.eval_chances_func(x)
    print("using bisector method value:\n\
            x = %s\n\
            f(x) = {very good aproval chance = %s,\n\
                    good aproval chance = %s,\n\
                    regular aproval chance = %s,\n\
                    bad aproval chance = %s,\n\
                    very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))

# Max method
def get_left_max(f, precission = 0.01):
    max_value = -1
    max_x = 0
    xs = np.arange(0, 100, precission)
    for x in xs:
        if f(x) > max_value:
            max_value = f(x)
            max_x = x
    return max_x
def get_right_max( f, precission = 0.01):
    max_value = -1
    max_x = 0
    xs = np.arange(0, 100, precission)
    for x in xs:
        if f(x) >= max_value:
            max_value = f(x)
            max_x = x
    return max_x
def get_median_max( f, precission = 0.01):
    xs = np.arange(0,100,precission)
    max_value = -1
    max_xs = []
    for x in xs:
        if f(x) > max_value:
            max_xs = [x]
            max_value = f(x)
        elif f(x) == max_value:
            max_xs.append(x)
    return max_xs[int(len(max_xs)/2)]

# Centroid
def centroid_method( f):
    f = f
    def func(x):
        return x*f(x)
    return integrate.quad(func, 0, 100)[0]/integrate.quad(f, 0, 100)[0]

# Bisector
def bisector_method( f):
    return _binary_search(f, 0, 100)
def _binary_search( f, a, b):
    m = (b + a)/2
    left_val = integrate.quad(f, 0, m)[0]
    right_val = integrate.quad(f, m, 100)[0]
    if abs(left_val - right_val) < 0.1:
        return m
    if left_val < right_val:
        return _binary_search(f, m, b)
    return _binary_search(f, a, m)
