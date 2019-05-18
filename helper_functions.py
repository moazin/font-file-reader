from collections import OrderedDict
from classes import *

def parseStructure(f, struct_table):
    results = OrderedDict()
    for key, value in struct_table.items():
        if isinstance(value, FieldType):
            results[key] = FieldData(value, f.read(value.size))
    return results

def parseArray(f, structure, count):
    results = []
    for i in range(count):
        results.append(parseStructure(f, structure))
    return results

def printTable(table_name, structure, table):
    print("{:^100}".format(table_name))
    print("-"*100)
    offset = 20
    first = False
    format_string = ""
    for key, val in structure.items():
        if first == False:
            format_string = "{:>0}"
        else:
            format_string += "{:>" + str(offset) + "}"
        first = True
    print(format_string.format(*[item[0] for item in structure.items()]))
    print("-"*100)
    for row in table:
        print(format_string.format(*[str(item[1]) for item in row.items()]))
