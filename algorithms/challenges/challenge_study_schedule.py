def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None
    counter = 0
    for a, b in permanence_period:
        if type(a) is not int or type(b) is not int:
            return None
        if target_time >= a and target_time <= b:
            counter += 1
    return counter
