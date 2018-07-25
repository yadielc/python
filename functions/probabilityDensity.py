# This is is a function that calculates the probability density function
# Here's a link to the equation https://en.wikipedia.org/wiki/Probability_density_function
def gaussian_density(x, mu, sigma):
    return (1/np.sqrt(2*np.pi*np.power(sigma, 2.))) * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sigma, 2.)))
