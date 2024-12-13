class Clock:
    """24-hour clock showing the hour and minute"""

    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def add(self, hours=0, minutes=0):
        """Add hours and minutes to the clock"""
        # Calculate extra hours from minutes overflow
        extra_hours = (self.minutes + minutes) // 60
        # Update minutes with the remaining value after overflow
        self.minutes = (self.minutes + minutes) % 60
        # Update hours with the added hours and any extra hours from minutes
        self.hours = (self.hours + hours + extra_hours) % 24

    def __str__(self):
        """Return a string representation of the clock in HH:MM format"""
        hour_str = str(self.hours).zfill(2)
        min_str = str(self.minutes).zfill(2)
        return f'{hour_str}:{min_str}'

    def __repr__(self):
        """Return a string representation of the clock object"""
        return f"Clock({self.hours}, {self.minutes})"

# Example usage:
clock = Clock(10, 30)
print(clock)  # Output: 10:30

clock.add(2, 40)
print(clock)  # Output: 13:10

clock.add(12, 90)
print(clock)  # Output: 02:40
