import csv
import numpy as np
instruction_list = []
ingrediant_list = []
name_list = []
with open('recpie/RAW_recipes.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for instruction in csv_reader:
        instruction_list.append(instruction[8])
        ingrediant_list.append(instruction[10])
        name_list.append(instruction[0])
def matching_ing(name):
    for id,ingrediant in enumerate(ingrediant_list):
        for ing1 in name:
            if ing1 in ingrediant:
                return (name_list[id],instruction_list[id])