# N represents the number of times you threw the die
def dice_rolls(N):
    roll_counts = [0,0,0,0,0,0]
    for i in range(N):
        roll = rd.choice([1,2,3,4,5,6])
        index = roll - 1
        roll_counts[index] = roll_counts[index] + 1
    return roll_counts

# function to show the information after tosssing the die
def roll_info(roll_counts):
    number_of_sides_on_die = len(roll_counts)
    for i in range(number_of_sides_on_die):
        number_of_rolls = roll_counts[i]
        number_on_die = i+1
        print(number_on_die, "came up", number_of_rolls, "times")

roll_data = dice_rolls(1000)
roll_info(roll_data)
