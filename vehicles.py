"""
File: vehicles.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #9
Task: Parent and Child classes
"""
from random import seed
from random import randint
seed(1)
randomCars = [
    ["Toyota", "Corolla", 2006, 400],
    ["Porsche", "Cayenne", 2010, 350],
    ["Ford", "Focus", 2012, 400],
    ["Mercedez", "S Class", 2010, 310],
    ["Honda", "Civic", 2009, 300],
    ["Ferarri", "Deno", 2010, 290]
]

randomPlanes = [
    ["Boeing", "747", 2001, 15000],
    ["Airbus", "A350", 2004, 18000],
    ["Concord", "M 232", 2003, 12000],
    ["Jetliner", "Bronco", 1999, 8000],
    ["Boeing", "737", 2007, 9800],
]


def createRandomCar(player):
    carData = randint(0, len(randomCars) - 1)
    print(carData)
    newCar = Cars(randomCars[carData][0], randomCars[carData]
                  [1], randomCars[carData][2], randomCars[carData][3])
    player.addCar(newCar)
    print(f"\n===-*!! Congrats {player.name}! You got a new Car !!*-===")
    print(newCar)
    input("\nPress any key to continue...")
    mainMenu(player)


def hwcreateRandomCar(player):
    carData = randint(0, len(randomCars) - 1)
    print(carData)
    newCar = Cars(randomCars[carData][0], randomCars[carData]
                  [1], randomCars[carData][2], randomCars[carData][3])
    player.addCar(newCar)
    print(f"\n===-*!! Congrats {player.name}! You got a new Car !!*-===")
    print(newCar)


def createRandomPlane(player):
    PlaneData = randint(0, len(randomPlanes) - 1)
    newPlane = Planes(randomPlanes[PlaneData][0], randomPlanes[PlaneData]
                      [1], randomPlanes[PlaneData][2], randomPlanes[PlaneData][3])
    player.addPlane(newPlane)
    print(f"\n===-*!! Congrats {player.name}! You got a new Plane !!*-===")
    print(newPlane)
    input("\nPress any key to continue...")
    mainMenu(player)


def hwcreateRandomPlane(player):
    PlaneData = randint(0, len(randomPlanes) - 1)
    newPlane = Planes(randomPlanes[PlaneData][0], randomPlanes[PlaneData]
                      [1], randomPlanes[PlaneData][2], randomPlanes[PlaneData][3])
    player.addPlane(newPlane)
    print(f"\n===-*!! Congrats {player.name}! You got a new Plane !!*-===")
    print(newPlane)


class Vehicle:
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0):
        self.model = Model
        self.make = Make
        self.year = Year
        self.weight = Weight
        self.needsMaintenance = NeedsMaintenance
        self.tripsSinceMaintenance = TripsSinceMaintenance

    def getMake(self):
        return self.make

    def setMake(self, Make):
        self.make = Make

    def getModel(self):
        return self.model

    def setModel(self, Model):
        self.model = Model

    def getYear(self):
        return self.year

    def setYear(self, Year):
        self.year = Year

    def getTripsSinceMaintenance(self):
        return self.tripsSinceMaintenance

    def getNeedsMaintenance(self):
        return self.needsMaintenance

    def getWeight(self):
        return self.weight

    def setWeight(self, Weight):
        self.weight = Weight

    def Repair(self):
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0


class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0, isDriving=False):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.isDriving = isDriving

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        self.isDriving = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

    def __str__(self):
        return (f"Vehicle Type: Car\nMake: {self.make}\nModel: {self.model}\nYear: {str(self.year)}\nWeight: {str(self.weight)} lbs\nIs Driving ? {str(self.isDriving)}\nTrips Since Maintenance: {str(self.tripsSinceMaintenance)}\nNeeds Maintenance ? {str(self.needsMaintenance)}")


class Planes(Vehicle):
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0, isFlying=False):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.isFlying = isFlying

    def Fly(self):
        if self.needsMaintenance:
            print(" - Sorry - Cannot fly without Maintenance first")
            self.isFlying = False
            return False
        else:
            print(
                f"{self.make} {self.model} flew on a trip around the world")
            self.isFlying = True

    def Land(self):
        if self.isFlying:
            self.isFlying = False
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance >= 100:
                self.needsMaintenance = True
        else:
            print("This plane isn't flying right now")

    def __str__(self):
        return (f"Vehicle Type: Plane\nMake: {self.make}\nModel: {self.model}\nYear: {str(self.year)}\nWeight: {str(self.weight)}lbs\nIs Currently Flying ? {str(self.isFlying)}\nTrips Since Maintenance: {str(self.tripsSinceMaintenance)}\nNeeds Maintenance ? {str(self.needsMaintenance)}")


class Player:
    def __init__(self, name="YourName", cars=[], planes=[], isDriving=False, isFlying=False):
        self.name = name
        self.cars = cars
        self.planes = planes
        self.isDriving = False
        self.isFlying = False

    def addCar(self, car):
        self.cars.append(car)

    def addPlane(self, plane):
        self.planes.append(plane)

    def __str__(self):
        return (f" - {self.name} currently has {len(self.cars)} cars and {len(self.planes)} planes\n - Is {self.name} driving right now ? {self.isDriving}\n - Is {self.name} flying right now ? {self.isFlying}")


def selectCar(player):
    if len(player.cars) > 0:
        if player.isDriving == False:
            print("\n==== Please select a Car ====")
            i = 1
            for car in player.cars:
                print(
                    f" [{i}] {car.make} {car.model}: Trips - {str(car.tripsSinceMaintenance)}. Needs Maintenance - {car.needsMaintenance}")
                i += 1
            selectedCarIndex = int(
                input(f"\nPlease Select A Car (1 - {len(player.cars)}): "))
            while selectedCarIndex not in range(len(player.cars) + 1):
                print("Sorry, I don't think you have that car in your garage")
                selectedCarIndex = int(
                    input(f"\nPlease Select A Car (1 - {len(player.cars)}): "))
            return selectedCarIndex - 1
        else:
            print(
                f" - But {player.name}, you're already driving the {str(player.cars[player.activeCarIndex].year)} {player.cars[player.activeCarIndex].make} {player.cars[player.activeCarIndex].model}")
            while True:
                stopDriving = input(" - Do you want to stop driving? (y/n): ")
                if stopDriving == "y" or stopDriving == "Y":
                    player.cars[player.activeCarIndex].Stop()
                    print(
                        f"\n - - {player.name} parked the {str(player.cars[player.activeCarIndex].year)} {player.cars[player.activeCarIndex].make} {player.cars[player.activeCarIndex].model} car back in the garage")
                    player.activeCarIndex = -1
                    player.isDriving = False
                    break
                elif stopDriving == "n" or stopDriving == "N":
                    print(
                        f" - - {player.name} continued cruising around in the {str(player.cars[player.activeCarIndex].year)} {player.cars[player.activeCarIndex].make} {player.cars[player.activeCarIndex].model}")
                    break
                else:
                    print("Please enter a valid option")
                    continue
            input("Press any key to continue...")
            mainMenu(player)
            # Stop driving


def selectPlane(player):
    if len(player.planes) > 0:
        if player.isFlying == False:
            print("\n==== Please select a Plane ====")
            i = 1
            for plane in player.planes:
                print(
                    f" [{i}] {plane.make} {plane.model}: Trips - {str(plane.tripsSinceMaintenance)}. Needs Maintenance - {plane.needsMaintenance}")
                i += 1
            selectedPlaneIndex = int(
                input(f"\nPlease Select A plane (from 1 - {len(player.planes)}): "))
            while selectedPlaneIndex not in range(len(player.planes) + 1):
                print("Sorry, I don't think you have that plane in your garage")
                selectedPlaneIndex = int(
                    input(f"\nPlease Select A plane (from 1 - {len(player.planes)}): "))
            return selectedPlaneIndex - 1
        else:
            print(
                f" - But {player.name}, you're already currently flying in the {str(player.planes[player.activePlaneIndex].year)} {player.planes[player.activePlaneIndex].make} {player.planes[player.activePlaneIndex].model}")
            while True:
                stopFlying = input("Do you want to land the Plane? (y/n): ")
                if stopFlying == "y" or stopFlying == "Y":
                    player.planes[player.activePlaneIndex].Land()
                    print(
                        f"\n - - {player.name}'s Pilot landed the {str(player.planes[player.activePlaneIndex].year)} {player.planes[player.activePlaneIndex].make} {player.planes[player.activePlaneIndex].model} plane at the nearest airport")
                    player.activePlaneIndex = -1
                    player.isFlying = False
                    break
                elif stopFlying == "n" or stopFlying == "N":
                    print(
                        f" - - {player.name} continued flying around the world in the {str(player.planes[player.activePlaneIndex].year)} {player.planes[player.activePlaneIndex].make} {player.planes[player.activePlaneIndex].model}")
                    break
                else:
                    print("Please enter a valid option")
                    continue
            input("Press any key to continue...")
            mainMenu(player)
            # Stop driving


def createNewCar(player):
    make = input(
        "(1/4) what is the make of the Car (e.g. Toyota, Mercedes, Ford)? ")
    model = input("(2/4) What is the model of the Car? ")
    year = input("(3/4) What year was the car made? ")
    weight = input("(4/4) What's the weight of the car (in pounds)? ")
    newCar = Cars(make, model, year, weight)
    player.addCar(newCar)
    print(f"\n===-*!! Congrats {player.name}! You got a new Car !!*-===")
    print(newCar)
    input("\nPress any key to continue...")
    mainMenu(player)


def createNewPlane(player):
    make = input(
        "(1/4) What is the make of the Plane (e.g. Airbus, Boeing, Concord)? ")
    model = input(
        "(2/4) What is the model of the plane (e.g. 737, A350, Bronco)? ")
    year = input("(3/4) What year was the plane made? ")
    weight = input("(4/4) What's the weight of the plane (in pounds)? ")
    newplane = Planes(make, model, year, weight)
    player.addPlane(newplane)
    print(f"\n===-*!! Congrats {player.name}! You got a new Plane !!*-===\n")
    print(newplane)
    input("\nPress any key to continue...")
    mainMenu(player)


def viewVehicles(player):
    print(f"\n======*** {player.name}'s Cars ***======")
    if len(player.cars) > 0:
        i = 1
        for car in player.cars:
            print(
                f"  [{i}] {car.make} {car.model}: Currently Driving - {str(car.isDriving)}. Trips - {str(car.tripsSinceMaintenance)}. Needs Maintenance - {car.needsMaintenance}")
            i += 1
    else:
        print(f" - Sorry you don't have any cars right now")
    print(f"\n======*** {player.name}'s Planes ***======")
    if len(player.planes) > 0:
        i = 1
        for plane in player.planes:
            print(
                f"  [{i}] {plane.make} {plane.model}: Currently Flying - {str(plane.isFlying)}. Trips - {str(plane.tripsSinceMaintenance)}. Needs Maintenance - {plane.needsMaintenance}")
            i += 1
    else:
        print(f" - Sorry, you don't have any planes right now\n")
    input("Press any key to continue...\n")
    mainMenu(player)


def driveMultiTrips(player):
    if len(player.cars) > 0:
        selectedCarIndex = selectCar(player)
        while True:
            noOfTrips = int(input("How many Trips will you be going on? "))
            if noOfTrips > 0:
                for i in range(noOfTrips):
                    player.cars[selectedCarIndex].Drive()
                    player.cars[selectedCarIndex].Stop()
                print(
                    f"\n - {player.name} drove the {str(player.cars[selectedCarIndex].year)} {player.cars[selectedCarIndex].make} {player.cars[selectedCarIndex].model} on {noOfTrips} Trips. What a nomad >.<\n")
                break
            else:
                print("Please enter a valid number > 0")
                continue
        if player.cars[selectedCarIndex].needsMaintenance:
            print(
                f" - Looks like this car (the {player.cars[selectedCarIndex].year} {player.cars[selectedCarIndex].make} {player.cars[selectedCarIndex].model}) needs maintenance - You should repair it.\n")
        input("Press any key to continue...\n")
        mainMenu(player)


def flyMultiTrips(player):
    if len(player.planes) > 0:
        selectedPlaneIndex = selectPlane(player)
        while True:
            noOfTrips = int(input("How many Trips will you be going on? "))
            if noOfTrips > 0:
                for i in range(noOfTrips):

                    player.planes[selectedPlaneIndex].Fly()
                    print(
                        f"That's {player.planes[selectedPlaneIndex].tripsSinceMaintenance} trips now")
                    player.planes[selectedPlaneIndex].Land()
                if player.planes[selectedPlaneIndex].tripsSinceMaintenance >= 100:
                    print(
                        f" - Pilots warning - The {player.planes[selectedPlaneIndex].year} {player.planes[selectedPlaneIndex].make} {player.planes[selectedPlaneIndex].model} needs maintenance. It can't fly without repairs!\n")
                    break
                else:
                    print(
                        f"\n - {player.name} flew the {str(player.planes[selectedPlaneIndex].year)} {player.planes[selectedPlaneIndex].make} {player.planes[selectedPlaneIndex].model} on {noOfTrips} Trips. What a nomad >.<\n")
                    break
            else:
                print("Please enter a valid number > 0")
                continue
        if player.planes[selectedPlaneIndex].needsMaintenance:
            print(
                f" - Looks like this plane (the {player.planes[selectedPlaneIndex].year} {player.planes[selectedPlaneIndex].make} {player.planes[selectedPlaneIndex].model}) needs maintenance - You should repair it.\n")
        input("Press any key to continue...\n")
        mainMenu(player)


def driveMenu(player):
    if len(player.cars) > 0:
        selectedCarIndex = selectCar(player)
        player.cars[selectedCarIndex].Drive()
        player.activeCarIndex = selectedCarIndex
        player.isDriving = True
        print(
            f"\n{player.name} is now driving the {str(player.cars[selectedCarIndex].year)} {player.cars[selectedCarIndex].make} {player.cars[selectedCarIndex].model} around - Such fun\n")
        input("Press any key to continue...\n")
        mainMenu(player)
    else:
        print(f" - Sorry you don't have any cars right now\n - Try Getting one from the Main menu")
        input("Press any key to continue...")
        mainMenu(player)


def flightMenu(player):
    if len(player.planes) > 0:
        selectedPlaneIndex = selectPlane(player)
        player.planes[selectedPlaneIndex].Fly()
        if player.planes[selectedPlaneIndex].isFlying:
            player.activePlaneIndex = selectedPlaneIndex
            player.isFlying = True
            print(
                f"\n - {player.name} is now flying around the world in his {str(player.planes[selectedPlaneIndex].year)} {player.planes[selectedPlaneIndex].make} {player.planes[selectedPlaneIndex].model}. much rich, such wow o.O!\n")
        else:
            print(
                f"\n - Pilots warning - The {player.planes[selectedPlaneIndex].year} {player.planes[selectedPlaneIndex].make} {player.planes[selectedPlaneIndex].model} needs maintenance. It can't fly without repairs!\n")
        input("Press any key to continue...\n")
        mainMenu(player)
    else:
        print(f" - Sorry you don't have any planes right now\n - Try Getting one from the Main menu")
        input("Press any key to continue...")
        mainMenu(player)


def repairVehicle(player):
    print("\n - - - Please select a Vehicle to repair: \n")
    i = 1
    if len(player.cars) > 0:
        for car in player.cars:
            print(
                f" [{i}] (car) {car.year} {car.make} {car.model} - {car.tripsSinceMaintenance} road trips since last Maintenance")
            i += 1
    if len(player.planes) > 0:
        for plane in player.planes:
            print(f" [{i}] (plane) {plane.year} {plane.make} {plane.model} - {plane.tripsSinceMaintenance} flights since last Maintenance")
            i += 1
    print(f" [{i}] Repair all {len(player.cars) + len(player.planes)} Vehicles")
    repairOption = int(input(f" Please enter selection (1 - {i}): "))
    if repairOption == i:
        if len(player.cars) > 0:
            for car in player.cars:
                if car.tripsSinceMaintenance > 0:
                    car.Repair()
                    print(
                        f" - The {car.year} {car.make} {car.model} car needed maintenance and was repaired!")
                else:
                    print(
                        f" - This car (the {car.year} {car.make} {car.model}) hasn't been on any trips yet, so does not need fixing/maintenance")
        if len(player.planes) > 0:
            for plane in player.planes:
                if plane.tripsSinceMaintenance > 0:
                    plane.Repair()
                    print(
                        f" - The {plane.year} {plane.make} {plane.model} plane needed maintenance and was repaired!")
                else:
                    print(
                        f" - This plane (the {plane.year} {plane.make} {plane.model}) hasn't been flown yet, so does not need fixing/maintenance")
        print(f"{player.name} had all vehicles repaired \n")
    elif repairOption < i and len(player.cars) >= repairOption:
        car = player.cars[repairOption-1]
        if player.cars[repairOption-1].tripsSinceMaintenance > 0:
            player.cars[repairOption-1].Repair()
            car = player.cars[repairOption-1]
            print(
                f" - The {car.year} {car.make} {car.model} car needed maintenance and was repaired!")
        else:
            print(
                f" - This car (the {car.year} {car.make} {car.model}) hasn't been on any trips yet, so does not need fixing/maintenance")
    elif repairOption < i and repairOption > len(player.cars) and repairOption <= (len(player.cars) + len(player.planes)):
        repairOption = repairOption - (len(player.cars))
        plane = player.planes[repairOption-1]
        if player.planes[repairOption-1].tripsSinceMaintenance > 0:
            player.planes[repairOption-1].Repair()
            print(
                f" - The {plane.year} {plane.make} {plane.model} plane needed maintenance and was repaired!")
        else:
            print(
                f" - This plane (the {plane.year} {plane.make} {plane.model}) hasn't been on any trips yet, so does not need fixing/maintenance")

    input("Press any key to continue...")
    mainMenu(player)


def perform(player, option):
    if option == "A" or option == "a":
        while True:
            vehicleType = int(input(
                "Please select type of Vehicle (1) Car (2) Plane: "))
            if vehicleType == 1:
                createNewCar(player)
                break
            elif vehicleType == 2:
                createNewPlane(player)
                break
            else:
                print("Please enter a valid Option (Ctrl + C) to exit")
                continue
    elif option == "B" or option == "b":
        while True:
            vehicleType = int(input(
                "Please select type of Vehicle (1) Car (2) Plane: "))
            if vehicleType == 1:
                createRandomCar(player)
                break
            elif vehicleType == 2:
                createRandomPlane(player)
                break
            else:
                print("Please enter a valid Option (Ctrl + C) to exit")
                continue
    elif option == "C" or option == "c":
        driveMenu(player)
    elif option == "D" or option == "d":
        flightMenu(player)
    elif option == "E" or option == "e":
        if len(player.cars) > 0:

            driveMultiTrips(player)
        else:
            print(
                f" - Sorry you don't have any cars right now\n - Try Getting one from the Main menu")
            input("Press any key to continue...")
            mainMenu(player)

    elif option == "F" or option == "f":
        if len(player.planes) > 0:

            flyMultiTrips(player)
        else:
            print(
                f" - Sorry you don't have any planes right now\n - Try Getting one from the Main menu")
            input("Press any key to continue...")
            mainMenu(player)
    elif option == "G" or option == "g":
        if len(player.planes) > 0 or len(player.cars) > 0:

            repairVehicle(player)
        else:
            print(
                f" - Sorry you don't have Cars or Planes right now\n - Try Getting a Car or a Plane from the Main menu")
            input("Press any key to continue...")
            mainMenu(player)
    elif option == "H" or option == "h":
        viewVehicles(player)
    elif option == "I" or option == "i":
        runAssignment(player)
        # print(option)
    else:
        print(option)


def mainMenu(player):
    menuOptions = ["A", "B", "C", "D", "E", "F", "G", "H",
                   "I", "a", "b", "c", "d", "e", "f", "g", "h", "i"]
    while True:
        print(f"What would you like to do {player.name}?")
        print(" [A] Get a new Car or Plane")
        print(" [B] Quickly clone a random car or plane")
        print(" [C] Drive / Stop Driving")
        print(" [D] Fly / Land")
        print(" [E] Drive Multiple Trips")
        print(" [F] Fly Multiple Trips")
        print(" [G] Repair A vehicle")
        print(" [H] View All Vehicles")
        print(" [I] View Pirple Assignment")
        option = input(
            f"\nPlease select an option (A - {menuOptions[len(menuOptions)-1]}): ")

        if option not in menuOptions:
            print("Sorry that option doesn't exist")
        else:
            perform(player, option)
            break


def runAssignment(player):
    player.cars = []
    player.planes = []
    player.isDriving = False
    player.isFlying = False
    print("\n- - - - * Pirple Assignment * - - - -")
    input(" - TASK [1] Create 3 cars (hit enter to continue...) ")
    hwcreateRandomCar(player)
    hwcreateRandomCar(player)
    hwcreateRandomCar(player)

    input("\n - TASK [2] Drive them around (hit enter to continue...) \n")
    for car in player.cars:
        randNoOfTrips = randint(0, 10)
        for i in range(randNoOfTrips):
            car.Drive()
            car.Stop()
        print(
            f" - {player.name} drove the {car.year} {car.make} {car.model} around on {randNoOfTrips} trips\n")

    input("\n - TASK [3] Print out Car Details (hit enter to continue...) ")
    print("-"*40)
    for car in player.cars:
        print(car)
        print("-"*40)

    input(
        "\n - TASK [4A] Extra Credit - Create 2 Planes (hit enter to continue...)")
    hwcreateRandomPlane(player)
    hwcreateRandomPlane(player)

    input(
        "\n - TASK [4B] Extra Credit - Fly Planes around till limit (100) (hit enter to continue...)")
    plane = player.planes[0]
    for i in range(105):
        plane.Fly()
        if plane.isFlying:
            print(f" - {plane.make} {plane.model} Flight no {i} - OK!")
        plane.Land()

    input(
        "\n - TASK [4C] Extra Credit - View All Vehicles (hit enter to continue...)")
    print(player)
    viewVehicles(player)


print("\n======== Welcome to Your New Garage =========")
playerName = input("Please enter your name: ")
player = Player(playerName)
mainMenu(player)
