def multiply_vectors(scalar, vector):
    new_vector = []
    for value in vector:
        new_value = scalar * value
        new_vector.append(new_value)
    return new_vector

vector = [1,2,3,4,5]
number = 3

product = multiply_vectors(number, vector)

print(number, "times", vector, "equals", product)
