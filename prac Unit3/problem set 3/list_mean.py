def list_mean(list):
    sum = 0
    for e in list:
        sum = sum + e
    mean = sum / len(list)
    return mean
