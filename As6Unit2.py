import json, csv, os, sys


def jsonCsv(filePath, csvName):         # convert file json -> csv
    json_file = open(filePath, 'r')
    csv_file = open(csvName, 'w')
    json_data = json.load(json_file)
    write = csv.writer(csv_file)            # use keys() and
    write.writerow(json_data.keys())        # values() to write the dictionary
    write.writerow(json_data.values())
    json_file.close()
    csv_file.close()


def csvJson(csv_file, json_file):         # convert file csv -> json
    jsonDict = {}
    with open(csv_file) as csvfile:
        csv_data = csv.DictReader(csvfile)  # Converting csv data into dictionary
        jsonDict['data'] = []
        for rows in csv_data:
            jsonDict['data'].append(rows)
    with open(json_file, 'w') as jsonfile:
        jsonfile.write(json.dumps(jsonDict, indent=4))      # Dumping the data into jsonfile


def checkCmd(cmd):          # check amount of argument
    if len(cmd) < 2:
        print('Not have path of folder')
        sys.exit()
    elif len(cmd) > 2:
        print('Only 2 arguments')
        sys.exit()


arg = sys.argv
checkCmd(arg)

for file in os.listdir():               # check type all file in folder (is json or csv)
    if file.endswith(".json"):
        newFile = file.split('.')[0] + '.csv'
        jsonCsv(file, newFile)
        os.remove(file)
    elif file.endswith(".csv"):
        newFile = file.split('.')[0] + '.json'
        csvJson(file, newFile)
        os.remove(file)