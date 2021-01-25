class SysTime:
    def __init__(self):
        pass

    def calc_time(self):
        os.system("py second.py")
        start_perf = time.perf_counter_ns()
        start_proc = time.process_time_ns()
        stop_perf = time.perf_counter_ns()
        stop_proc = time.process_time_ns()
        print(f'Performace time:{stop_perf-start_perf}\n'
              f'System time:{start_proc-stop_proc}')