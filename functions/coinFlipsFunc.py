“””” This a simple function that simulates the toss of a coinself.
     The initial number of trials is 100 but you can call this function
     with the number of trials you desire.
“””
import random as rd

def coin_flips(num_trials):
    heads = 0
    tails = 0
    p_heads = 0.5
    for i in range(num_trials):
        random_number = rd.random()
        if random_number < p_heads:
            heads = heads + 1
        else:
            tails += 1
    percent_heads = heads / num_trials
    return percent_heads

percentage = coin_flips(200) # calling the function and storing the result on variable
print(percentage)
