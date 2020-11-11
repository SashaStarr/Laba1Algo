import time

class Results:
    def __init__(self, name_farm):
        self.name = name_farm
        self.start_time = time.time()
        self.comparisons = 0
        self.swaps = 0

    def get_work_time(self):
        work_time = time.time() - self.start_time
        return work_time

    def number_of_comparisons(self):
        self.comparisons += 1

    def number_of_swaps(self):
        self.swaps += 1

    def statistic(self):
        print(self.name)
        print("Full work time :", self.get_work_time())
        print("Comparisons :", self.comparisons)
        print("Swaps :", self.swaps)