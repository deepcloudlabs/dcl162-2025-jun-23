"""
  Logistics -> Vehicle
"""


class OverCapacityError(Exception):
    """
    OverCapacityError: Sub-class/Derived-Class
    Exception -> Super-class/Base class for all exceptions in this module.
    """
    def __init__(self, message, over_weight):
        super().__init__(message)
        self.over_weight = over_weight


class Vehicle(object):
    """
    members:
        1. attributes: field -> data: __license_plate, __capacity, __current_load, __color
        2. behaviors: constructor (__init__),[business] methods -> load, unload
        3. property: object -> field -> method, read-only property -> current_load, capacity
                                                read-write property -> color, license_plate
    """

    # constructor -> object -> Heap [fields]
    def __init__(self, license_plate, capacity, current_load, color):
        self.__license_plate = license_plate
        self.__capacity = capacity
        self.__current_load = current_load
        self.__color = color

    @property
    def current_load(self):
        return self.__current_load

    @property
    def capacity(self):
        return self.__capacity

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        # validation/business rule/invariants/policy/regulations/...
        self.__color = new_color



    def load(self, weight):
        """
        business method: loads weight to the vehicle
        :param weight: in kg and must be positive
        :return: returns the current weight in kg
        """
        # validation
        if weight <= 0:
            raise ValueError(f"weight ({weight}) must be positive number.")
        # business rule/policy/regulation
        if self.__current_load + weight > self.__capacity:
            message = f"Vehicle {self.__license_plate} is over capacity."
            over_weight = self.capacity - self.__current_load - weight
            raise OverCapacityError(message, over_weight)
        self.__current_load += weight
        return self.__current_load

    def unload(self, weight):
        """
        business method: unloads weight from the vehicle
        :param weight: in kg and must be positive
        :return: returns the current weight in kg
        """
        # validation
        if weight <= 0:
            raise ValueError(f"weight ({weight}) must be positive number.")
        # validation
        if weight > self.current_load:
            raise ValueError(f"weight ({weight}) must be less than or equal to the current load({self.current_load}).")
        self.__current_load -= weight
        return self.__current_load

    def __str__(self):
        return f"Vehicle: {self.__license_plate}, {self.__color}, {self.__current_load} kg."


try:
    vehicle1 = Vehicle("32ABC42", 10_000, 0, "red")
    vehicle2 = Vehicle("32ABC43", 8_000, 0, "blue")
    vehicle1.load(2_000) # load(self=vehicle1, weight=2_000)
    Vehicle.load(self=vehicle2,weight=3_000) # vehicle2.load(3_000)
    print(f"vehicle2's current load is {vehicle2.current_load} kg.") # read
    vehicle2.load(3_000)
    vehicle1.load(4_000)
    #vehicle2.load(4_000)
    vehicle1.load(4_000)
    #vehicle2.load(2_000)
    vehicle1.color = "white" # write
    print(vehicle1)
except OverCapacityError as oce:
    print(oce)
except ValueError as ve:
    print(ve)
finally:
    vehicle1.unload(vehicle1.current_load)
    vehicle2.unload(vehicle2.current_load)
print(str(vehicle1))
print(vehicle2)