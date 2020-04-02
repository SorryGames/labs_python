import time

class Progressbar:
    return_symbol = "\033[F"
    """ 0 <= status <= 100 """
    def __init__(self, description="Loading"):
        self.count_grid = 50
        self.start = time.perf_counter()
        self.description = description
        self.show(0)

    def update(self, value, maxvalue=100):
        status = int(100 * value / maxvalue)
        status = min(status, 100)
        status = max(status, 0)
        print((Progressbar.return_symbol) * 5)
        self.show(status)

    def show(self, status):
        old_status = status
        status >>= 1
        #
        cur_time = int(time.perf_counter() - self.start)
        description = self.description + ("." * (cur_time % 3 + 1)) + "   "
        # show progressbar
        progress = ("[{}".format("#" * status)
                        + "{}]".format("." * (self.count_grid - status))
                        + " {}% ".format(old_status)
                        + "({}:{})".format(cur_time // 60, cur_time % 60)
                        + "   ")
        print("\n" + description + "\n" + progress + "\n")


if __name__ == "__main__":
    test = Progressbar()
    for i in range(0, 100000001):
        test.update(i, 100000001)