import time


class TrafficLight:

    __color = ""

    def running(self):
        while True:
            self.__color = "red"
            print(f"\033[31m{self.__color}")
            time.sleep(7)
            self.__color = "yellow"
            print(f"\033[33m{self.__color}")
            time.sleep(2)
            self.__color = "green"
            print(f"\033[32m{self.__color}")
            time.sleep(10)


light = TrafficLight()
light.running()
