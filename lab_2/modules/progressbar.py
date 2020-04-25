import time
import threading


class Progressbar:
    return_symbol = "\033[F"
    """ 0 <= status <= 100 """
    def __init__(self, description="Loading"):
        self.status = 0
        self.max_grid = 50
        self.description = description
        self.start = time.perf_counter()
        self.update_thread = threading.Thread(target=self._update)
        self.update_thread.start()

    def update(self, value, maxvalue=100):
        self.status = int(100 * value / maxvalue)
        self.status = min(self.status, 100)
        self.status = max(self.status, 0)

    def _update(self):
        while True:
            status = self.status
            count_grid = status >> 1
            #
            cur_time = int(time.perf_counter() - self.start)
            description = self.description + ("." * (cur_time % 3 + 1))
            description = description + "     "
            #
            progress = ("[{}".format("#" * count_grid)
                            + "{}]".format("." * (self.max_grid - count_grid))
                            + " {}% ".format(status)
                            + "({}:{})".format(cur_time // 60, cur_time % 60)
                            + "   ")
            print("\n" + description + "\n" + progress + "\n")
            #
            if status < 100: 
                print((self.return_symbol) * 5)
            else:
                break
            #
            time.sleep(1)

    def finish(self):
        self.status = 100
        self.update_thread.join()

if __name__ == "__main__":
    test = Progressbar()
    for i in range(0, 10000001):
        test.update(i, 10000000)