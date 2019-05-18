from collections import OrderedDict
from classes import *

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

svg_table_header = OrderedDict()
svg_table_header['version'] = NumberFieldType(2)
svg_table_header['offsetToSVGDocumentList'] = NumberFieldType(4)
svg_table_header['reserved'] = NumberFieldType(4)

svg_document_list = OrderedDict()
svg_document_list['numEntries'] = NumberFieldType(2)


svg_document_record = OrderedDict()
svg_document_record['startGlyphID'] = NumberFieldType(2)
svg_document_record['endGlyphID'] = NumberFieldType(2)
svg_document_record['svgDocOffset'] = NumberFieldType(4)
svg_document_record['svgDocLength'] = NumberFieldType(4)





