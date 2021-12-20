class A:
    def init(self, age, height, weight, number):
        self.age = age
        self.height = height
        self.weight = weight
        self.number = number
    def average(self):
        return float(self.age/self.number), float(self.height/self.number), float(self.weight/self.number)


class B:
    def init(self, age, height, weight, number):
        self.age = age
        self.height = height
        self.weight = weight
        self.number = number
    def average(self):
        return float(self.age/self.number), float(self.height/self.number), float(self.weight/self.number)

a = 0
h = 0
w = 0
ageA = 0.0
heightA = 0.0
weightA = 0.0
ageB = 0.0
heightB = 0.0
weightB = 0.0


for i in range(2):
    number = int(input(""))
    age = input()
    height = input()
    weigth = input()
    a = 0
    h = 0
    w = 0
    for item in age.split(" "):
        a += int(item)

    for item in height.split(" "):
        h += int(item)

    for item in weigth.split(" "):
        w += int(item)

    if i == 0:
        obj = A()
        ageA, heightA, weightA = obj.average()
    if i == 1:
        obj = B()
        ageB, heightB, weightB = obj.average()

print(ageA)
print(heightA)
print(weightA)
print(ageB)
print(heightB)
print(weightB)

if heightA == heightB:
    if weightA < weightB :
        print(weightA)
    elif weightB < weightA:
        print(weightB)
    else:
        print("Same")
elif heightA < heightB:
    print("B")
else:
    print("A")