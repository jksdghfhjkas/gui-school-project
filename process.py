import psutil

class CpuBar:
    def __init__(self):
        self.cpu_count = psutil.cpu_count(logical=False)
        self.cpu_count_logical = psutil.cpu_count()

    def cpu_percent_return(self):
        return psutil.cpu_percent(percpu=True)

    def ram_downloads_return(self):
        return psutil.virtual_memory()

    def cpu_one_return(self):
        return psutil.cpu_percent()





