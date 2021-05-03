import scheduler_functions as sf

def fcfs(init_processes):
    time_elapsed = 0
    active_process = None
    total_length = len(init_processes)
    arrived_processes = []
    finished_processes = []

    while(len(finished_processes) < total_length):

        # increments one waiting time for each non active process that has arrived
        sf.increment_wait(arrived_processes)

        # bursts active process
        sf.burst(active_process)

        # moves process to finished if process is done
        # sets active_process to None if done
        active_process = sf.is_process_done(active_process, finished_processes, time_elapsed)

        # transfers processes in a list when it has arrived
        sf.check_arrived(init_processes, arrived_processes, time_elapsed)

        # sorts and sets any arrived processes as active if there are no active processes
        active_process = sf.npe_next_process('fcfs', active_process, arrived_processes)

        time_elapsed += 1

    return finished_processes


def sjf(init_processes):
    time_elapsed = 0
    active_process = None
    total_length = len(init_processes)
    arrived_processes = []
    finished_processes = []

    while(len(finished_processes) < total_length):

        # increments one waiting time for each non active process that has arrived
        sf.increment_wait(arrived_processes)

        # bursts active process
        sf.burst(active_process)

        # moves process to finished if process is done
        # sets active_process to None if done
        active_process = sf.is_process_done(active_process, finished_processes, time_elapsed)

        # transfers processes in a list when it has arrived
        sf.check_arrived(init_processes, arrived_processes, time_elapsed)

        # sets any arrived processes as active if there are no active processes
        active_process = sf.npe_next_process('sjf', active_process, arrived_processes)
        
        time_elapsed += 1

    return finished_processes

def priority(init_processes):
    print("waw priority")

def srpt(init_processes):
    print("waw srpt")

def round_robin(init_processes):
    print("Waw round robin")