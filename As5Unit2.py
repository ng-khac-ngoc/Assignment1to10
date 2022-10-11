import argparse, csv, json, pandas, pathlib

parser = argparse.ArgumentParser(description='File format convert')
parser.add_argument('--input', '--input', type=str, help='File input to convert')
parser.add_argument('--output', '--output', type=str, help='File output to convert')
args = parser.parse_args()


def json_to_csv(file_path, csv_name):       # convert file json -> csv
    json_file = open(file_path, 'r')     # open file json and read
    csv_file = open(csv_name, 'w')      # open file csv and write
    json_data = json.load(json_file)
    write = csv.writer(csv_file)
    write.writerow(json_data.keys())         # use keys() and
    write.writerow(json_data.values())      # values() to write the dictionary
    json_file.close()
    csv_file.close()


def csv_to_json(csv_file, json_file):           # convert file csv -> json
    jsonDict = {}
    with open(csv_file) as csvfile:
        csv_data = csv.DictReader(csvfile)  # Converting the csv data into dictionary
        jsonDict['data'] = []
        for rows in csv_data:
            jsonDict['data'].append(rows)  # Append csv row in json dictionary
    with open(json_file, 'w') as jsonfile:
        jsonfile.write(json.dumps(jsonDict, indent=4))  # Dumping the data into jsonfile


def json_to_xlsx(json_file, xlsx_file):
    pandas.read_json(json_file).to_excel(xlsx_file)


def xlsx_to_json(xlsx_file, json_file):
    pandas.read_excel(xlsx_file).to_json(json_file)


with pathlib.Path(args.input) as f:
    if f.is_file():
        if args.input.find('json') != -1:
            if args.output.find('csv') != -1:
                json_to_csv(args.input, args.output)
            else:
                json_to_xlsx(args.input, args.output)
        elif args.input.find('csv') != -1:
            csv_to_json(args.input, args.output)
        else:
            xlsx_to_json(args.input, args.output)
    else:
        print(f'Did not find {args.input}')