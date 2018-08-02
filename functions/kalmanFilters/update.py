
def update(mean1, variance1, mean2, variance2):
    new_mean = (variance2 * mean1 + variance1 * mean2)/ (var1 + var2)
    new_var = 1/ (1/var1 + 1/ var2)
    return [new_mean, new_var]
