"""
Exercise 4: Counter Class

Create a `Counter` class with:
- Class attribute: total_counters (tracks how many counters created)
- Instance attribute: count (starts at 0)
- Methods:
  - increment() - add 1 to count
  - decrement() - subtract 1 from count
  - reset() - set count to 0
  - get_count() - return current count
- Class method: get_total_counters()
"""

# TODO: Write your Counter class here
class Counter:
    total_counters = 0  # Class attribute to track total counters created

    def __init__(self):
        self.count = 0  # Instance attribute to track individual count
        Counter.total_counters += 1  # Increment total counters when a new instance is created

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

    @classmethod
    def get_total_counters(cls):
        return cls.total_counters
# Test code (uncomment when ready)
c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
c1.increment()
c2.decrement()
print(f"Counter 2: {c2.get_count()}")
print(f"Counter 1: {c1.get_count()}")
print(f"Total counters: {Counter.get_total_counters()}")
