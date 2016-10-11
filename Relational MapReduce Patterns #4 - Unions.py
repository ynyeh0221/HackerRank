# Enter your code here. Read input from STDIN. Print output to STDOUT
# This template is based on the framework supplied for a similar challenge, in a Coursera Data Science course: https://www.coursera.org/course/datasci
# And the code supplied here: https://github.com/uwescience/datasci_course_materials/blob/master/assignment3/wordcount.py
# The map-reduce emulator is provided
# You need to fill out the mapper and reducer functions

import json
import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        jenc = json.JSONEncoder()
        for item in self.result:
            print str(item[1])

mapReducer = MapReduce()

def mapper(record):
    key = record["key"]
    value = record["value"]
    mapReducer.emitIntermediate(key, value)

def reducer(key, list_of_values):
    for i in mapReducer.result:
         if i[1] == list_of_values[0]:
            return
    mapReducer.emit((key, list_of_values[0]))


if __name__ == '__main__':
    inputData = []
    counter = 0
    Nr = Ns = 0
    for line in sys.stdin:
        counter += 1
        line = line[:-1]
        if counter == 1:
            [Nr,Ns] = map(int, line.split())
        else:
            inputData.append(json.dumps({"key":counter,"value":int(line)}))
    mapReducer.execute(inputData, mapper, reducer)
