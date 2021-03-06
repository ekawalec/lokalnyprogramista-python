import os
class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.name = ""
        self.direction = "N"

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        self.say_state()
        self.say_direction()

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"
        self.say_state()
        self.say_direction()

    def say_direction(self):
        print("[" + self.name + "] moj aktualny kierunek: {}".format(self.direction))

    def say_state(self):
        print("[" + self.name + "] moja aktualna prędkość: {} km/h!".format(self.speed))

    def accelerate(self):
        self.speed += 5
        self.say_state()
        self.say_direction()

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5
        self.say_state()
        self.say_direction()

    def hand_brake(self):
        self.speed = 0
        self.say_state()
        self.say_direction()

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
           pass
        # powyższe 2 linie są w sumie niepotrzebne, ale pass jako polecenie moze kiedys sie przydac

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
        if action not in "WSQEXHAD" or len(action) != 1:
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
        elif action == 'H':
            os.system('cls')
            myCar.hand_brake()
        elif action == 'A':
            os.system('cls')
            myCar.turn_left()
        elif action == 'D':
            os.system('cls')
            myCar.turn_right()
        elif action == 'X':
            os.system('cls')
            print(" ... astalavista baby ....")
            exit()
        myCar.step()