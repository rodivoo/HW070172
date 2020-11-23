import re
import yaml

"""
1. load bibtex file
    - bibliography should be curated in Zotero (one can program cleaning procedures into the script, but this is not as reliable);
    - loading bibtex data, keep only those records that have PDFs;
    - some processing might be necessary (like picking one file out of two and more)
2. convert into other formats
    - csv
    - json
    - yml
"""

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml"
settings = yaml.load(open(settingsFile))
bibKeys = yaml.load(open("zotero_biblatex_keys.yml"))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(bibTexFile):
    # create dictionary bibDic
    bibDic = {}
    # open the file 
    with open(bibTexFile, "r", encoding="utf8") as f1:
        # read the file and split the string by "\n@" => list
        records = f1.read().split("\n@")
        # loop through each list item - start with the second one
        for record in records[1:]:
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():
                # split the string by "\n" - end with the second last => list; Remove spaces at the beginning and the end
                record = record.strip().split("\n")[:-1]
                # split record[0] by "{" and save the first item (inlcuding remove spaces)
                rType = record[0].split("{")[0].strip()
                # split record[0] by "{" and save the second item (inlcuding remove spaces and replace ",")
                rCite = record[0].split("{")[1].strip().replace(",", "")
                # create nested dictionary rCite in bibDic
                bibDic[rCite] = {}
                # save rCite in the nested dictionary rCite
                bibDic[rCite]["rCite"] = rCite
                # save rType in the nested dictionary rCite
                bibDic[rCite]["rType"] = rType
                # loop through each list item - start with the second one
                for r in record[1:]:
                    # split the string by "=" and save the first item (inlcuding remove spaces)
                    key = r.split("=")[0].strip()
                    # split the string by "=" and save the second item (inlcuding remove spaces)
                    val = r.split("=")[1].strip()
                    # remove { and } form the second item
                    val = re.sub("^\{|\},?", "", val)
                    # save bibKeys[key] to fixedKey
                    fixedKey = bibKeys[key]
                    # save val to bibDic[rCite][fixedKey]
                    bibDic[rCite][fixedKey] = val


    print("="*80)
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic))
    print("="*80)
    # return dictionary bibDic
    return(bibDic)

# CONVERSION FUNCTIONS

import json
def convertToJSON(bibTexFile):
    # call the function bibLoad with the filename as input value and save the return value to data
    data = bibLoad(bibTexFile)
    # create or open the file zotero_biblatex_sample.json
    with open(bibTexFile.replace(".bib", ".json"), 'w', encoding='utf8') as f9:
        # write data to the file
        json.dump(data, f9, sort_keys=True, indent=4, ensure_ascii=False)


import yaml
def convertToYAML(bibTexFile):
    # call the function bibLoad with the filename as input value and save the return value to data
    data = bibLoad(bibTexFile)
    # create or open the file zotero_biblatex_sample.bib
    with open(bibTexFile.replace(".bib", ".yaml"), 'w', encoding='utf8') as f9:
        # write data to the file
        yaml.dump(data, f9)

# CSV is the trickest because bibTeX is not symmetrical
def convertToCSV(bibTexFile):
    # call the function bibLoad with the filename as input value and save the return value to data
    data = bibLoad(bibTexFile)
    # let's handpick fields that we want to save: citeKey, type, author, title, date
    headerList = ['citeKey', 'type', 'author', 'title', 'date']
    # string created by joining the items of headerList (separator \t)
    header = "\t".join(headerList)
    #create list dataNew
    dataNew = [header]
    # loop through all items of the dictionry data
    for k,v in data.items():
        # variable k as citeKey
        citeKey = k
        # check if rType is present in the dictionary
        if 'rType' in v:
            # if true: save v['rType'] to variable rType
            rType = v['rType']
        else:
            # if false: not available
            rType = "NA"
        # check if author is present in the dictionary
        if 'author' in v:
            # if true: save v['author'] to variable author
            author = v['author']
        else:
            # if false: not available
            author = "NA"
        # check if title is present in the dictionary
        if 'title' in v:
            # if true: save v['title'] to variable title
            title = v['title']
        else:
            # if false: not available
            title = "NA"
        # check if date is present in the dictionary
        if 'date' in v:
            # if true: save v['date'] to variable date
            date = v['date']
        else:
            # if false: not available
            date = "NA"
        # string tempVal created by joining the items of the list (separator \t)
        tempVal = "\t".join([citeKey, rType, author, title, date])
        # appending the strings tempVal to the list dataNew
        dataNew.append(tempVal)        
    # string finalData created by joining the items of the list dataNew (separator \t)
    finalData = "\n".join(dataNew)
    # create or open the file zotero_biblatex_sample.csv
    with open(bibTexFile.replace(".bib", ".csv"), 'w', encoding='utf8') as f9:
        # write finalData to the file
        f9.write(finalData)

###########################################################
# RUN EVERYTHING ##########################################
###########################################################

#print(settings["bib_all"])

# call the function convertToJSON with the filename as input value
#convertToJSON(settings["bib_all"])
# call the function convertToYAML with the filename as input value
#convertToYAML(settings["bib_all"])
# call the function convertToCSV with the filename as input value
convertToCSV(settings["bib_all"])

print("Done!")