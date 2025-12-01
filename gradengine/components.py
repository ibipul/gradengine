import math
import numpy as np

class Node:
    def __init__(self,data):
        self.data = data
        self.grad = 0.0

    def __repr__(self):
        return f"Node(data={self.data})"

