# import numpy as np
# import matplotlib.pyplot as plt
# def sigmoid(x):
#     return 1 / (1+ np.exp(-x))
# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
# plt.plot(x,y)
# plt.ylim(-0.1, 1.1)
# plt.show()
#
import numpy as np
#
# def andPerceptron(x1, x2):
#     w1, w2, theta = 0.5, 0.5, 0.7
#     netInput = x1*w1 + x2*w2
#     if netInput <= theta:
#         return 0
#     elif netInput > theta:
#         return 1
#
# def nandPerceptron(x1, x2):
#     w1, w2, theta = -0.5, -0.5, -0.7
#     netInput = x1*w1 + x2*w2
#     if netInput <= theta:
#         return 0
#     elif netInput > theta:
#         return 1
#
# def orPerceptron(x1, x2):
#     w1, w2, bias = 0.5, 0.5, -0.2
#     netInput = x1*w1 + x2*w2 + bias
#     if netInput <= 0:
#         return 0
#     else:
#         return 1
#
# inputData = np.array([[0,0],[0,1],[1,0],[1,1]])
#
# print("---And Perceptron---")
# for xs1 in inputData:
#     print(str(xs1) + " ==> " + str(andPerceptron(xs1[0], xs1[1])))
#
# print("---Nand Perceptron---")
# for xs2 in inputData:
#     print(str(xs2) + " ==> " + str(nandPerceptron(xs2[0], xs2[1])))
#
# print("---Or Perceptron---")
# for xs3 in inputData:
#     print(str(xs3) + " ==> " + str(orPerceptron(xs3[0], xs3[1])))
# a= 22+2j
# print(type(a))

import numpy as np
import matplotlib.pylab as plt


# def step_function(x):
#     return np.array(x > 0, dtype=np.int)
#
# x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)
# plt.show()
#

def step_function(x):
    y = x > 0
    return y.astype(np.int)

# def sigmoid(x):
#     return 1/(1+np.exp(-x))
# x = np.arange(-5.0,5.0,0.1)
# y = step_function(x)
# plt.plot(x,y)
# plt.show()

# x0, x1, x2 = -1, 0, 0
# w0, w1, w2 = .3, .4, .1
#
# x = np.array([x0,x1,x2])
# w = np.array([w0,w1,w2])
# a = np.sum(x*w)
# def step(x):
#     y = x > 0
#     return y.astype(np.int)
#
# print(step(a))


# o=step_function()
# print(np.sum(step_function(x0*w0),step_function(x1*w1),step_function(x2*w2)))

#
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
#
#
# x = np.array([1.0, 2.0])
# print(sigmoid(x))
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
#
#
# x = np.arange(-8.0, 8.0, 0.1)
# y = sigmoid(-x)
#
# plt.plot(x, y)
# plt.show()


def relu(x):
    return np.maximum(0, x)


print(relu(-2))

print(relu(0.3))
