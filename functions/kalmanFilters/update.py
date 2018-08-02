'''
Update Step in Kalman Filters
'''
def update(mean1, variance1, mean2, variance2):
    new_mean = (variance2 * mean1 + variance1 * mean2)/ (var1 + var2)
    new_variance = 1/ (1/var1 + 1/ var2)
    return [new_mean, new_variance]

print update(5., 7., 14., 2.)

def predict(mean1, variance1, mean2, variance2):
    new_mean = mean1 + mean2
    new_variance = variance1 + variance2
    return [new_mean, new_variance]


print predict(10., 4., 12., 4.)
