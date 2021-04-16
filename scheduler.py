
def fcfs(init_processes):
    time_elapsed = 0
    total_length = len(init_processes)
    arrived_processes = []
    finished_processes = []
    while(len(finished_processes) < total_length):
        for process in init_processes:
            if process.arrival_time == time_elapsed:
                arrived_processes.append(process)
                init_processes.remove(process)

        time_elapsed += 1
def sjf(init_processes):
    print("waw sjf")

def priority(init_processes):
    print("waw priority")

def srpt(init_processes):
    print("waw srpt")

def round_robin(init_processes):
    print("Waw round robin")