import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('Advertising.csv', delimiter=',')
m, n = data.shape
X = data[:, 0:n-1]
Y = data[:, n-1].reshape((m, 1))
ones = np.ones((m, 1))
X = np.hstack((ones, X))

iterations = 500        # gradient descent iterations count
alpha = 0.01            # learning rate

theta = np.random.rand(n, 1)

def plotData():
    # get rid of X_0 constants column
    features = X[:, 1: n]
    plt.figure(1)

    plt.subplot(131)
    plt.plot(features[:, 0], Y, 'bo')
    plt.title('TV')
    plt.ylabel('Sales')

    plt.subplot(132)
    plt.plot(features[:, 1], Y, 'ro')
    plt.title('Radio')
    plt.ylabel('Sales')

    plt.subplot(133)
    plt.plot(features[:, 2], Y, 'yo')
    plt.title('Newspaper')
    plt.ylabel('Sales')

    plt.show()

def computeCost():
    hypothesis = np.dot(X, theta);
    delta = np.dot((hypothesis - Y).transpose(), (hypothesis - Y))
    return (1 / m) * delta


def normalizeFeatures():
    mu = np.ones((1, n))
    sigma = np.ones((1, n))
    for i in range(1,n):
        mu[0][i] = np.mean(X[:, i])
        sigma[0][i] = np.std(X[:, i])
        X[:, i] = (X[:, i] - mu[0][i]) / sigma[0][i]

    return mu, sigma;

# gradientDescent() calculates hypothesis equation coefficients using gradient descent algorithm
def gradientDescent(theta):
    # vector to keep track of progression of cost function with each iteration
    J_history = np.ones((iterations, 1))
    plt.plot(np.linspace(0,iterations, iterations), J_history)
    plt.title('Cost function against number of iterations')
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost function J(theta)')
    plt.show()
    return

# normalEquation() calculates hypothesis equation coefficients analytically
def normalEquation():
    A = np.linalg.pinv(np.dot(X.transpose(), X))
    B = np.dot(X.transpose(), Y)
    theta = np.dot(A, B)

    return theta

def predict(x_vector, mu, sigma):
    # scale feature vector
    for i in range(1, n):
        x_vector[0][i] = (x_vector[0,i]- mu[0][i]) / sigma[0][i]

    return np.dot(x_vector, theta)
if __name__ == '__main__':
    plotData()
    mu, sigma = normalizeFeatures()
    gradientDescent(theta)

    prediction_vector = np.array([1, 40, 40, 48]).reshape(1,4)