# Pets class getters and setters
class Pet:
    def __init__(self, n, a, h, p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

    # Setters
    def setName(self, Name):
        self.name = name

    def setAge(self, Age):
        self.age = Age

    def setHunger(self, Hunger):
        self.hunger = Hunger

    def setPlayful(self, Playful):
        self.playful = Playful


# Create Dog class as a child class of pet
class Dog(Pet):
    def __init__(self, n, a, h, p, b, f):
        Pet.__init__(self, n, a, h, p)
        self.breed = b
        self.favoriteToy = f

    def wantsToPlay(self):
        if self.playful:
            return (self.name + " the dog wants to play with " + self.favoriteToy)
        else:
            return (self.name + " the dog doesn't want to play")


class Cat(Pet):
    def __init__(self, n, a, h, p, fp):
        Pet.__init__(self, n, a, h, p)
        self.favoritePlaceToSit = fp

    def wantsToSit(self):
        if self.playful == False:
            print(self.name + " the Cat wants to sit in " +
                  self.favoritePlaceToSit)
        else:
            print(self.name + " the Cat wants to play")

    def __str__(self):
        return (self.name + " the" + str(self.age) + "yr old cat, likes to sit in " + self.favoritePlaceToSit)


class Human:
    def __init__(self, name, Pets):
        self.name = name
        self.Pets = Pets

    def hasPets(self):
        if len(self.Pets) > 0:
            return "yes"
        else:
            return "no"


HuskyDog = Dog("Jim", 5, False, True, "Husky", "Plushy")
TomCat = Cat("Tom", 3, False, False, "The kitty Pool")
Alice = Human("Alice", [HuskyDog, TomCat])

print(Alice.hasPets())

print(HuskyDog.wantsToPlay())
TomCat.wantsToSit()

print(TomCat)
