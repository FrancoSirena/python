class Classy:
    def __init__(self, name, age=10, height=1):
        self.name = name
        self.age = age
        self.height = height
class Timer:
    def __init__(self, time):
        self.time = time
    def forward(self, n):
        self.time = self.time + n
    def backward(self, n):
        self.time = self.time - n
class DoubleTimer(Timer):
    def forward(self, n):
        self.time = self.time + n * 2
    def backward(self, n):
        self.time = self.time - n * 2
