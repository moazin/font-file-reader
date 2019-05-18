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

    def getData(self):
        return self.field_type.getData(self)
    def __str__(self):
        return self.field_type.getStr(self)

    __repr__ = __str__
