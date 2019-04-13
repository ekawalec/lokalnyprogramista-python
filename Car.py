import os
class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.name = ""

    def say_state(self):
        print("[" + self.name + "] moja aktualna prędkość: {} km/h!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':

    myCar = Car()
    os.system('cls')
    print("Siema, to ja twoje AUTO! Co mam teraz zrobić?")
    myCar.name = input("Nadaj mi jakieś imię: ")
    print("Podoba mi się {} :)".format(myCar.name))
    while True:
        print(" ")
        print("---------------------------------------------------------------------------------------------------------")
        print("[W] przyspiesz   |   [S] zwolnij   |   [Q] przebieg   |   [E] średnia prędkość   |   [X] koniec programu")
        print("---------------------------------------------------------------------------------------------------------")
        action = input("Twój wybór: ").upper()
        if action not in "WSQEX" or len(action) != 1:
            os.system('cls')
            print("Nie wiem jak mam to wykonać")
            continue
        if action == 'W':
            os.system('cls')
            myCar.accelerate()
        elif action == 'S':
            os.system('cls')
            myCar.brake()
        elif action == 'Q':
            os.system('cls')
            print("Aktualny przebieg: {} km".format(myCar.odometer))
        elif action == 'E':
            os.system('cls')
            print("Srednia prędkość: {} km/h".format(myCar.average_speed()))
        elif action == 'X':
            os.system('cls')
            print(" ... astalavista baby ....")
            exit()
        myCar.step()
        myCar.say_state()