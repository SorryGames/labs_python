import time

class Progressbar:
    """ 0 <= status <= 100 """
    def __init__(self):
        self.count_grid = 50
        self.start = time.perf_counter()
        self.show(0)

    def update(self, value, maxvalue=100):
        status = int(100 * value / maxvalue)
        status = min(status, 100)
        status = max(status, 0)
        print("\033[F" * 4)
        self.show(status)

    def show(self, status):
        old_status = status
        status >>= 1
        cur_time = int(time.perf_counter() - self.start)
        # show progressbar
        progress = "[{}".format("#" * status)\
                        + "{}]".format("." * (self.count_grid - status))\
                        + " {}% ".format(old_status)\
                        + "({}:{})".format(cur_time // 60, cur_time % 60)
        print("\n" + progress + "\n")


if __name__ == "__main__":
    test = Progressbar()
    for i in range(0, 1000000):
        test.update(i, 1000000)