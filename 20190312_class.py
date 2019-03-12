# 建立類別
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# 從類別建立實例
my_dog = Dog('胖達', 3)
print("我的狗的名字叫做 " + my_dog.name)
print("他 " + str(my_dog.age) + " 歲")

my_dog.sit()
my_dog.roll_over()

# 類別運用
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 設定預設值

    def get_descriptive_name(self): # 讀取屬性方法
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' +self.make + ' ' + self.model
        return long_name

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) +
        " miles on it.")

    def fill_gas_tank(self):
        print("加油囉!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.increment_odometer(1000)
my_new_car.read_odometer()

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) +
        "-kWh battery.")

# 繼承
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self): # 覆寫父類別
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # 把實例當成屬性
my_tesla.fill_gas_tank()