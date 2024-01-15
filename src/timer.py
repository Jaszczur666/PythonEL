import time


def wait(duration):
    time.sleep(duration / 1e3)


class TimeManager:
    def __init__(self):
        self.time_of_start = (
            time.time()
        )  # to be reset later, initially will hold time of initialization
        self.ticks = 0

    def time_elapsed(self):
        return time.time() - self.time_of_start

    def tick(self):
        self.ticks += 1

    def start_timer(self):
        self.time_of_start = time.time()

    def seconds_per_tick(self):
        return self.time_elapsed()/self.ticks


if __name__ == "__main__":
    tm = TimeManager()
    for i in range(20):
        print(i, tm.ticks,  tm.time_elapsed())
        wait(215)
        tm.tick()
    print(tm.seconds_per_tick())
