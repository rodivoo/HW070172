# convert.py
# A program to convert a bibliography in bibTeX format into csv/tsv, json, and yaml

import json
import yaml
import pandas

def main():
    with open("bibliography.bib", "r") as readfile:
        contents = readfile.read()
    myDictionary = {}
    contents = contents[:-2]
    contents = contents.split("\n@")
    for x in contents[1:]:
        x = x[:-2]
        x = x.split(",\n")
        for y in x:
            if y == x[0]:
                y = y.split("{")
                myDictionary[y[1]] = {}
                myDictionary[y[1]]["recordType"] = y[0]
                z = y[1]
            else:
                y = y.split("=")
                myDictionary[z][y[0].strip()] = y[1].strip()
    
    with open("bibliography.json", "w") as outfile:  
        json.dump(myDictionary, outfile)

    with open("bibliography.yaml", "w") as outfile:  
        yaml.dump(myDictionary, outfile)

    data = pandas.DataFrame.from_dict(myDictionary, orient='index')
    data.to_csv('bibliography.csv')

main()