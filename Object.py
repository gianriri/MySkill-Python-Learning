class Car:
    # Properti
    type = "Fiat"
    model = "500"
    color = "white"

    #Method
    def start(self):
        print("ini method start")

    def drive(self):
        print("ini method drive")

    def brake(self):
        print("ini method brake")

    def stop(self):
        print("ini method stop")

    # Membuat objek mobil
car = Car()
print(car.type)
print(car.color)

    # Memanggil method car.start()
car.drive()
car.brake()
car.stop()

class Person:
    # Konstruktor
    def __init__(self, firstName, lastName):
        # Properti
        self.firstName = firstName
        self.lastName = lastName

    # Method
    def full_name(self):
        return f"{self.firstName} {self.lastName}"
    
    def show_name(self):
        print(self.full_name())

# Mmebuat objek Person
person1 = Person("Muhar", "Tony")
person2 = Person("Petani", "Kode")

# Memanggil method
person1.show_name()
person2.show_name()