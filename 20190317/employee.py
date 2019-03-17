class Employee():
    """Create an employee."""

    def __init__(self, first, last, salary):
        """Store employees' firstname, lastname and salary."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, how_much=5000):
        """Add employees' salary."""
        self.salary += how_much