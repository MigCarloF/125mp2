class Process:

    def __init__(self, process_number: int, arrival_time: int, burst_time: int, priority: int):
        self.process_number = process_number
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.time_remaining = burst_time

    def display(self):
        print("Process number: %d\nArrival Time: %d\nBurst Time: %d\nPriority: %d\nWaiting Time: %d\nTurnaround Time: %d\n" %
        (self.process_number, self.arrival_time, self.burst_time, self.priority, self.waiting_time, self.turnaround_time) )

    def burst(self):
        if(self.time_remaining < 1):
            raise BurstException
        self.time_remaining -= 1

    def wait(self):
        self.waiting_time += 1

    def is_done(self):
        return self.time_remaining == 0

    def finish(self, time_finished):
        self.turnaround_time = time_finished

class BurstException(Exception):
    """Thrown when attempting to burst a process with time_remaining at 0"""
