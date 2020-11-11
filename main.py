import csv
from sort import *
from model.farm import *


def parse_csv(path):
    farm_arr = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for i in csv_reader:
            farm_arr.append(Farm(i[0], int(i[1]), int(i[2])))
    return farm_arr

if __name__ == '__main__':

    farmers = parse_csv('farm_list.csv')
    print_array(farmers)

    sort_fan_power_in_watts_des(farmers)
    print_array(farmers)

    sort_number_of_animals_asc(farmers)
    print_array(farmers)
