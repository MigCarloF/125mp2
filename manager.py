from process import Process
from typing import List
import scheduler

# Handles all process creation and decisions
def run(filename, scheduling):
    try:
        initial_processes = create_processes(filename)
    except ValueQuantityException:
        print("Number of values per line is incorrect")
        quit()
    except IncorrectFirstRowException:
        print("First Line must contain Process, Arrival, CPU Burst, Time, and Priority!")
        quit()

    finished_processes = handle_scheduling_choice(initial_processes, scheduling)
    
    print("\nFinished Processes:\n")
    for process in finished_processes:
        process.display()

# Returns list of processes
def create_processes(filename) -> List[Process]:
    processes = []

    with open(filename, 'r') as file:

        line = file.readline()
        first_row = line.split()

        # checks if first line are the appropriate labels
        if(first_row.__str__() != "['Process', 'Arrival', 'CPU', 'Burst', 'Time', 'Priority']"):
            raise IncorrectFirstRowException

        # reads a file line by line until line is empty
        while True:
            line = file.readline()
            data: List[str] = line.split()
            if(len(line) <= 0):
                break

            # checks if there are exactly 4 values to compare
            if(len(data) != 4):
                raise ValueQuantityException

            processes.append(create_process(data))

    return processes

def create_process(data: List[str]) -> Process:
    process_number = int(data[0])
    arrival_time = int(data[1])
    burst_time = int(data[2])
    priority = int(data[3])
    return Process(process_number, arrival_time, burst_time, priority)

# Returns a list of processes processed by a scheduler
def handle_scheduling_choice(initial_processes: List[Process], scheduling: str) -> List[Process]:    
    if scheduling == 'fcfs':
        return scheduler.fcfs(initial_processes)

    if scheduling == 'sjf':
        return scheduler.sjf(initial_processes)

    if scheduling == 'priority':
        return scheduler.priority(initial_processes)

    if scheduling == 'srpt':
        return scheduler.srpt(initial_processes)

    if scheduling == 'round_robin':
        return scheduler.round_robin(initial_processes)
    else:
        print("Invalid state")
        return None


class ValueQuantityException(Exception):
    """Raised when the number of values in the file is too small or too large"""
    pass

class IncorrectFirstRowException(Exception):
    """Raised when input has incorrect first row"""
    pass