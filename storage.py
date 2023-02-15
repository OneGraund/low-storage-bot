import shutil


class Storage:
    def __init__(self, low_prc_left=5, low_gib_left=10):
        print('Storage class created')
        total, used, free = shutil.disk_usage("/")
        self.total = total // (2 ** 30)
        self.used = used // (2 ** 30)
        self.free = free // (2 ** 30)
        self.low_prc_left = low_prc_left
        self.low_gib_left = low_gib_left

    def __str__(self):
        return (f"Total: {self.total} GiB" + '\n' +
                f"Used: {self.used} GiB" + '\n' +
                f"Free: {self.free} GiB")

    def return_prc_left(self):
        return 100 - ((self.used * 100) / self.total)

    def is_enough_prc(self):
        left = self.return_prc_left()
        if left <= self.low_prc_left:
            return False
        else:
            return True

    def is_enough_gib(self):
        if self.free <= self.low_gib_left:
            return False
        else:
            return True
