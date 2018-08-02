

def update(mean1, variance1, mean2, variance2):
    new_mean = float(variance2 * mean1 + variance1 * mean2) / (variance1 + variance2)
    new_variance = 1./(1./variance1 + 1./variance2)
    return [new_mean, new_variance]

def predict(mean1, variance1, mean2, variance2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for n in range(len(measurements)):
    [mu, sigma] = update(mu, sigma, measurements[n], measurement_sigma )
    print 'update: ', [mu, sigma]
    [mu, sigma] = predict(mu, sigma, motion[n], motion_sigma)
    print 'predict: ', [mu, sigma]



print [mu, sigma]
