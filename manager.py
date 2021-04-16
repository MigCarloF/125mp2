from process import Process
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

    if scheduling == 'fcfs':
        scheduler.fcfs(initial_processes)
    elif scheduling == 'sjf':
        scheduler.sjf(init_processes)
    elif scheduling == 'priority':
        scheduler.priority(init_processes)
    elif scheduling == 'srpt':
        scheduler.srpt(init_processes)
    elif scheduling == 'round_robin':
        scheduler.round_robin(init_processes)
    else:
        print("Invalid state")


# Returns list of processes
def create_processes(filename):

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
            data = line.split()
            if(len(line) <= 0):
                break

            # checks if there are exactly 4 values to compare
            if(len(data) != 4):
                raise ValueQuantityException

            processes.append(create_process(data))

    return processes

def create_process(data):
    process_number = int(data[0])
    arrival_time = int(data[1])
    burst_time = int(data[2])
    priority = int(data[3])
    return Process(process_number, arrival_time, burst_time, priority)


class ValueQuantityException(Exception):
    """Raised when the number of values in the file is too small or too large"""
    pass

class IncorrectFirstRowException(Exception):
    """Raised when input has incorrect first row"""
    pass