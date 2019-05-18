from collections import OrderedDict

class FieldType:
    def __init__(self, size):
        self.size = size

class AsciiFieldType(FieldType):
    @classmethod
    def getData(cls, data_field):
        return (data_field.byte_string).decode('ascii')

    @classmethod
    def getStr(cls, data_field):
        return cls.getData(data_field)


class NumberFieldType(FieldType):
    @classmethod
    def getData(cls, data_field):
        return int.from_bytes(data_field.byte_string, byteorder='big')

    @classmethod
    def getStr(cls, data_field):
        return str(cls.getData(data_field))


class HexFieldType(FieldType):
    @classmethod
    def getData(cls, data_field):
        return hex(int.from_bytes(data_field.byte_string, byteorder='big'))

    @classmethod
    def getStr(cls, data_field):
        return str(cls.getData(data_field))

class FieldData:
    def __init__(self, field_type, byte_string):
        self.field_type = field_type
        self.byte_string = byte_string

    def __str__(self):
        return self.field_type.getStr(self)

    __repr__ = __str__

# Structure to handle offset_table
offset_table = OrderedDict()
offset_table['sfntVersion'] = HexFieldType(4)
offset_table['numTables'] = NumberFieldType(2)
offset_table['searchRange'] = NumberFieldType(2)
offset_table['entrySelector'] = NumberFieldType(2)
offset_table['rangeShift'] =  NumberFieldType(2)

# Structure to handle a Table Record in dir_tables
table_record = OrderedDict()
table_record['tableTag'] = AsciiFieldType(4)
table_record['checkSum'] = HexFieldType(4)
table_record['offset'] = NumberFieldType(4)
table_record['length'] = NumberFieldType(4)



file_name = "gilbert.otf"

f = open(file_name, 'rb')

results = OrderedDict()

def parseStructure(struct_table):
    results = OrderedDict()
    for key, value in struct_table.items():
        if isinstance(value, FieldType):
            results[key] = FieldData(value, f.read(value.size))
    return results

def parseArray(structure, count):
    results = []
    for i in range(count):
        results.append(parseStructure(structure))
    return results

offset_tabl = parseStructure(offset_table)

table_records = parseArray(table_record, 14);

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


fs = printTable("Offsets Table", offset_table, [offset_tabl])

fs = printTable("Dir Table", table_record, table_records)


