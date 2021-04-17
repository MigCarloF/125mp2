# increments one waiting time for each non active process that has arrived
def increment_wait(processes):
    for process in processes:
        process.wait()

# transfers initial processes to arrived processes if arrived
def check_arrived(init_processes, arrived_processes, time_elapsed):
    appended_processes = []
    for process in init_processes:
        if process.arrival_time == time_elapsed:
            arrived_processes.append(process)
            appended_processes.append(process)

    for process in appended_processes:
        init_processes.remove(process)

# sets any arrived processes as active if there are no active processes
# returns active process if there is stil an active process
def set_active(active_process, arrived_processes):
    if(active_process == None and len(arrived_processes) > 0):
        return arrived_processes.pop(0)
    return active_process

# bursts active process while checking for null
def burst(active_process):
    if(active_process != None):
            active_process.burst()

# returns none if process is done else returns the process
def is_process_done(active_process, finished_processes, time_elapsed):
    if(active_process != None and active_process.is_done()):
        finished_processes.append(active_process)
        active_process.turnaround_time = time_elapsed
        return None
    return active_process