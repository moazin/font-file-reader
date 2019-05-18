from classes import AsciiFieldType, NumberFieldType, HexFieldType, FieldData, FieldType
from helper_functions import parseStructure, parseArray, printTable
import table_structures as ts

file_name = "gilbert.otf"

f = open(file_name, 'rb')


offset_tabl = parseStructure(f, ts.offset_table)
table_records = parseArray(f, ts.table_record, offset_tabl['numTables'].getData());
#fs = printTable("Offsets Table", ts.offset_table, [offset_tabl])
#fs = printTable("Dir Table", ts.table_record, table_records)

offset_to_svg = None
for row in table_records:
    if row['tableTag'].getData() == 'SVG ':
        offset_to_svg = row['offset'].getData()
f.seek(offset_to_svg)

header = parseStructure(f, ts.svg_table_header) 

offset_to_svg_doc_list = header['offsetToSVGDocumentList'].getData() + offset_to_svg

f.seek(offset_to_svg_doc_list)

svg_doc_list = parseStructure(f, ts.svg_document_list)

num_svg_records = svg_doc_list['numEntries'].getData()

records = parseArray(f, ts.svg_document_record, num_svg_records)

printTable('SVG Records', ts.svg_document_record, records)

# grab record 1 say!
for i in range(10):
    row = records[i]
    offset_to_doc = row['svgDocOffset'].getData() + offset_to_svg_doc_list
    svg_doc_length = row['svgDocLength'].getData()
    f.seek(offset_to_doc)
    document = (f.read(svg_doc_length)).decode('ascii')
    print("\n")
    print("\n")
    print(document)
