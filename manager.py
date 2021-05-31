from process import Process
from typing import List
import copy
import scheduler

# Handles all process creation and decisions
def run(filename):
    try:
        initial_processes = create_processes(filename)
    except ValueQuantityException:
        print("Number of values per line is incorrect")
        quit()
    except IncorrectFirstRowException:
        print("First Line must contain Process, Arrival, CPU Burst, Time, and Priority!")
        quit()

    fcfs_processes = handle_scheduling_choice(copy.deepcopy(initial_processes), 'fcfs')
    sjf_processes = handle_scheduling_choice(copy.deepcopy(initial_processes), 'sjf')
    srpt_processes = handle_scheduling_choice(copy.deepcopy(initial_processes), 'srpt')
    priority_processes = handle_scheduling_choice(copy.deepcopy(initial_processes), 'priority')
    round_robin_processes = handle_scheduling_choice(copy.deepcopy(initial_processes), 'round_robin')

    evaluate_processes(fcfs_processes, 'fcfs')
    evaluate_processes(sjf_processes, 'sjf')
    evaluate_processes(srpt_processes, 'srpt') 
    evaluate_processes(priority_processes, 'priority')
    evaluate_processes(round_robin_processes, 'round_robin')

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

def evaluate_processes(processes: List[Process], scheduling):
    averages = average_times(processes)

    print("For %s:" % (scheduling))
    print("Turnaround Time: %d" % averages[0])
    print("Average Waiting Time: %d" % averages[1])
    print()




# returns average turnaround time
def average_times(processes: List[Process]):
    average_turnaround_time = 0
    average_waiting_time = 0

    for process in processes:
        average_turnaround_time += process.turnaround_time

    for process in processes:
        average_waiting_time += process.waiting_time
    
    average_turnaround_time /= len(processes)
    average_waiting_time /= len(processes)

    return [average_turnaround_time, average_waiting_time]

class ValueQuantityException(Exception):
    """Raised when the number of values in the file is too small or too large"""
    pass

class IncorrectFirstRowException(Exception):
    """Raised when input has incorrect first row"""
    pass