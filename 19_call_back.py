

class MUltiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return   value * self.factor

five_times = MUltiplier(5)

print(callable(five_times))

result = five_times(10)

print(result)