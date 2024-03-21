#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def greedy(capacity, items):
    current_weight = 0
    items_taken = [0]*len(items)
    value = 0
    counter = 0
    value_weight_ratios = []

    for item in items:
        value_weight_ratios.append(item.value / item.weight)

    while current_weight < capacity:
        next_item_index = np.argmax(value_weight_ratios)

        if items[next_item_index].weight + current_weight < capacity:
            items_taken[next_item_index] = 1
            value += items[next_item_index].value
            current_weight += items[next_item_index].weight

        else:
            counter += 1

        value_weight_ratios[next_item_index] = 0
        
        if counter == len(items):
            break
    
    return items_taken, value



def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    taken, value = greedy(capacity, items)
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

