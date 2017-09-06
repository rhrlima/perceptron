"""
Perceptron classifier made with Python3 and Pygame
Author: Ricardo Henrique Remes de Lima <https://www.github.com/rhrlima>
"""

from dependencies import *


class LineEquation:

	def __init__(self, m, b):
		self.m = m
		self.b = b

	def getY(self, x):
		return self.m * x + self.b


class Point:

	def __init__(self, x, y, label=0):
		self.x = x
		self.y = y
		self.label = 1 if label < y else -1
		self.color = WHITE


class Perceptron2D:

	def __init__(self, lrate=0):
		self.lrate = lrate
		self.weights = [0] * 3

		self.init_weights()

	def init_weights(self):
		for i, w in enumerate(self.weights):
			self.weights[i] = random.uniform(-1, 1)

	def train(self, inputs, target):
		guess = self.classify(inputs)
		error = target - guess
		for i, o in enumerate(inputs):
			self.weights[i] += self.lrate * error * inputs[i]
		self.weights[len(inputs)] += self.lrate * error #bias

	def classify(self, inputs):
		inputs += (1,)
		sum = 0
		for i, w in zip(inputs, self.weights):
			sum += w * i
		return 1 if sum >= 0 else -1

	def guess_line(self, x):
		w0 = self.weights[0]
		w1 = self.weights[1]
		w2 = self.weights[2]

		return - (w0 / w1) * x -(w2 / w1)