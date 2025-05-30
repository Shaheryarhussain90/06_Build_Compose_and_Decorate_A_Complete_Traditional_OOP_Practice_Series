class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod

    def show_counter(cls):
            print(f"Total Object Cretef: {cls.count}")
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.show_counter()