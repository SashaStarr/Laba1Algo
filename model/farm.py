class Farm(object):
    def __init__(self,location = "USA" , number_of_animals = 60 ,fan_power_in_watts = 20) :
        self.location = location
        self.number_of_animals = number_of_animals
        self.fan_power_in_watts = fan_power_in_watts
    def __str__(self):
        return "location= " + self.location +  ", number of animals= " + str(self.number_of_animals) +\
               ", fan power in watts= " + str(self.fan_power_in_watts)
    