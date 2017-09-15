# Perceptron

Implementation of the Perceptron classifier using Pygame to display the learning and classification process.

This code was created following the videos from the [Coding Train](https://www.youtube.com/user/shiffman) channel.

## Getting Started

Instructions needed to run the project.

### Prerequisites

This code requires Python3 and Pygame to run.

### Installing

* [Python3](https://www.python.org/download/releases/3.0/) - Python Website.

* [Pip](https://pip.pypa.io/en/stable/installing/) - Package Installer for Python.

* [Pygame](https://www.pygame.org/news) - The Pygame library website.

Install pygame by running the following:

```
pip install -r requirements.txt
```

### Running

To run the game, call:

```
python main.py
```

## Parameters

Inside main.py we have:

* WIDTH: window width
* HEIGHT: window height

* FPS: frames per second
* POINT_SIZE: size of the points

* NUM_POINTS: size of the dataset
* LEARNING_RATE: learning rate

Also, during the execution the user can interact with the classifier with:

* LEFT MOUSE BUTTON: add new point at the cursor's position.
* RIGHT MOUSE BUTTON: generate new dataset with different line equation.

## Example

![Example](https://raw.githubusercontent.com/rhrlima/perceptron/master/img/ex1.png)
