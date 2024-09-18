import numpy as np
                                                        # Dataset (population, profit)
x_train = np.array([6.1101, 5.5277, 8.5186, 7.0032, 5.8598, 8.3829, 7.4764, 8.5781, 6.4862, 5.0546])
y_train = np.array([17.592, 9.1302, 13.662, 11.854, 6.8233, 11.886, 4.3483, 12, 6.5987, 3.8166])

                                         # Initialize parameters
w = 0                                                    # Weight (slope)
b = 0                                                    # Bias (intercept)
alpha = 0.01                                             # Learning rate
iterations = 1000                                        # Number of iterations for gradient descent
m = len(x_train)                                         # Number of training examples
                                        # Gradient descent loop                                                                           
for _ in range(iterations):  
    y_pred = w * x_train + b                              # Predicting values
                                                          
    dw = (1 / m) * np.dot(x_train, (y_pred - y_train))    # Compute gradients
    db = (1 / m) * np.sum(y_pred - y_train)
    
    w -= alpha * dw                                       # Update parameters
    b -= alpha * db

                                        # Final values of w and b
print(f"Final weight (w): {w}, Final bias (b): {b}")
                                                         # Predict profit for a population of 35,000
population = 3.5                                          # Population in 10,000s
profit = w * population + b
print(f"Predicted profit for population 35,000: {profit * 10000:.2f}")
