import csv
import json



CSV_FILE_PATH = '/data/orders_messy.csv'
JSON_FILE_PATH = '/data/orders_clean.json'

#cleanining the data, for example, remove empty rows, strip whitespace, etc.
def normalize_name(raw):
    return raw.lower().strip().replace(' ', '')

def parse_amount(raw):
    try:
        return float(raw.replace('$', '').replace(',', '').replace(' ', '').replace('N/A', ''))
    except ValueError:
        return None
    
#def parse_email(raw):
#    if '@' in raw:
#        return raw.lower().strip()
#    return None


#def parse_date(raw):
#    try:
#        return date(raw.strip())
#    except ValueError:
#        return None

def parse_quantity(raw):
    try:
        return int(raw.strip().isdigit())
    except ValueError:
        return None
    
def read_csv(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, mode='r',  newline='', encoding='utf-8') as f:
            r= csv.DictReader(f)
            csv_clean = []
            for row in r:
                #methods to clean the data, for example, remove empty rows, strip whitespace, etc.
                #header: order_id,customer_name,email,order_date,amount,quantity,status,notes
                csv_clean.append({
                    'order_id': row['order_id'].lower().strip().replace(' ', ''),
                    'customer_name': normalize_name(row['customer_name']),
                    #'email': parse_email(row['email']),
                    #'order_date': parse_date(row['order_date']),
                    'amount': parse_amount(row['amount']),
                    'quantity': parse_quantity(row['quantity']),
                    'status': row['status'].lower().strip().replace(' ', ''),
                    'notes': row['notes'].lower().strip()
                })
            return csv_clean
        
 #convert csv to json, how to do that?
 # read csv_clean and convert to json format, then write to a json file
 #error handling on file writing
def main():
    try:
        csv_clean = read_csv(CSV_FILE_PATH)
        print(f"Read {len(csv_clean)} rows from {CSV_FILE_PATH}")
    except Exception as e:
        print(f"Error reading {CSV_FILE_PATH}: {e}")


if __name__ == "__main__":
    main()
