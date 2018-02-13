import csv
import json

def first_line_of_csv(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)
        row1 = next(reader)
    return row1

def sanitise_names(headers):
    new_headers = []
    for header in headers:
        new_headers.append(
            header.replace(".", "_").strip())
    return new_headers

def headers_to_schema(csvfile, required = ['CompanyNumber']):
    headers = first_line_of_csv(csvfile)
    headers = sanitise_names(headers)
    schema = [{"name": header.strip(),
               "description": header.strip(),
               "type": "STRING",
               "mode": "NULLABLE"} for header in headers]
    for obj in schema:
        if obj['name'] in required:
            obj['mode'] = 'REQUIRED'
    return schema

def csv_to_json_schema(csvfile, outfile, required = ['CompanyNumber']):
    schema = headers_to_schema(csvfile, required)
    with open(outfile, 'w') as f:
        json.dump(schema, f)

def load_schema(schema = "company_data_schema.json"):
    with open(schema, 'r') as f:
        tbl_schema = json.load(f)
    return tbl_schema

def list_columns_by_type(schema, col_type="DATE", names_only = True):
    """
    Return a list of columns by type from
    a GBQ schema
    """
    cols = []
    for col in schema:
        if col['type'] == col_type:
            cols.append(col)
    if names_only:
        return [col['name'] for col in cols]
    else:
        return cols



