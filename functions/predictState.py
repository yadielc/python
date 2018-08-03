

def predictState(state, dt):
    # Assume that state takes the form [x, vel] i.e. [0, 50]



    distance = state[0] + state[1] * dt;

    predicted_x = distance - state[1]*dt;
    predicted_vel = state[0] - 1/dt;

    # Constructs the predicted state and returns it
    predicted_state = [predicted_x, predicted_vel]
    return predicted_state



test_state = [10, 3]
test_dt = 5

test_output = predictState(test_state, test_dt)
