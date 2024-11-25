import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        voin = 100
        counter = 0

        print(f"{self.name} , на нас напали!")
        while voin:
            voin -= self.power
            counter += 1
            time.sleep(1)
            print(f"{self.name} сражается {counter} дней, осталось воинов {voin}\n")
            

        else:
            print(f"{self.name} одержал победу спустя {counter}")



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()



