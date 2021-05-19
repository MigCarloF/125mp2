from typing import List
from process import Process

# General scheduler functions


# increments one waiting time for each non active process that has arrived
def increment_wait(processes: List[Process]):
    for process in processes:
        process.wait()

# transfers initial processes to arrived processes if arrived
def check_arrived(init_processes, arrived_processes, time_elapsed):

    # checks each process if arrived. Transfers to arrived list if it did
    for process in init_processes:
        if process.arrival_time == time_elapsed:
            arrived_processes.append(process)
            init_processes.remove(process)


# non-pre emptive
# sorts all arrived processes
# sets next process as active according to scheduling if there are no active processes
# returns active process if there is stil an active process
def npe_next_process(scheduling: str, active_process, arrived_processes: List[Process]):
    if(active_process == None and len(arrived_processes) > 0):
        sort(arrived_processes, scheduling)
        next_process = arrived_processes.pop(0)
        return next_process
    return active_process

# srpt only
# sorts all arrived processes
# puts active process back in to be sorted
# sets head of array as next process after sort
# returns active process if there are no arrived processes
def srpt_next_process(scheduling: str, active_process: Process, arrived_processes: List[Process]):
    if(len(arrived_processes) > 0):
        if active_process != None:
            arrived_processes.insert(0, active_process)
        sort(arrived_processes, scheduling)
        next_process = arrived_processes.pop(0)
        return next_process
    return active_process


# rr only
# sets active process if none
# when time done is  4, adds it to end of list 
# sets head of list as active
def rr_next_process(scheduling: str, active_process: Process, arrived_processes: List[Process], time_elapsed):
    if len(arrived_processes) > 0:
        if active_process == None:
            return arrived_processes.pop(0)
        if active_process.rr_time_last_checked == 4:
            active_process.swap_turn()
            swap = active_process
            active_process = arrived_processes.pop(0)
            arrived_processes.append(swap)
            return active_process
    return active_process

# bursts active process while checking for null
def burst(active_process: Process):
    if(active_process != None):
            active_process.burst()

# returns none if process is done else returns the process
def is_process_done(active_process, finished_processes, time_elapsed):
    if(active_process != None and active_process.is_done()):
        finished_processes.append(active_process)
        active_process.turnaround_time = time_elapsed
        return None
    return active_process

def sort(processes: List[Process], scheduling: str) -> List[Process]:
    if(scheduling == 'fcfs'):
        # Do nothing
        pass
    
    if(scheduling == 'sjf'):
        processes.sort(key=lambda x: x.burst_time)

    if(scheduling == 'priority'):
        processes.sort(key=lambda x: x.priority)

    if(scheduling == 'srpt'):
        processes.sort(key=lambda x: x.time_remaining)


