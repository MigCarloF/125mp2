class Process:

    def __init__(self, process_number, arrival_time, burst_time, priority):
        self.process_number = process_number
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.active = False