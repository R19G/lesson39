from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100

    def notification_start(self):
        f"{self.name}, на нас напали!"

    def notification_end(self):
        f"{self.name} одержал победу спустя {self.days} дней(дня)!"

    def run(self):
        self.notification_start()
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            print(f'{self.name}, сражается {self.days} день(дня), осталось {self.enemies} воинов.')
            sleep(1)
        self.notification_end()


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')