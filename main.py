import csv
import json


CSV_FILE_PATH = 'order_messy.csv'
JSON_FILE_PATH = 'order_clean.json'

#lookup how to read csv file
#

def read_csv(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, mode='r') as csvfile:
            csv_messy = csv.reader(csvfile, delimiter=',')
            csv_clean = []
            for row in csv_messy:
                #methods to clean the data, for example, remove empty rows, strip whitespace, etc.
                csv_clean.append(row)
        
 #convert csv to json, how to do that?
 # read csv_clean and convert to json format, then write to a json file
 #error handling on file writing
def main():
    print("file successfully written to ", JSON_FILE_PATH)


if __name__ == "__main__":
    main()
