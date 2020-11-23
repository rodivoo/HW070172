import os, yaml

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml"
vars = yaml.load(open(settingsFile))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# analyze bibTeX data; identify what needs to be fixed

def bibAnalyze(bibTexFile):
    # create dictionary tempDic
    tempDic = {}
    # open the file 
    with open(bibTexFile, "r", encoding="utf8") as f1:
        # read the file => string
        records = f1.read()
        # split the string by "\n@" => list
        records = records.split("\n@")
        # loop through each list item - start with the second one
        for record in records[1:]:
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():
                # remove spaces at the beginning and the end
                record = record.strip()
                # split the string by "\n" - end with the second last => list
                record = record.split("\n")[:-1]
                # loop through each list item - start with the second one
                for r in record[1:]:
                    # split the string by "=" => list, save the first list item and remove spaces at the beginning and the end
                    r = r.split("=")[0].strip()
                    # check if r is present in the dictionary
                    if r in tempDic:
                        # if true: increment tempDic[r]
                        tempDic[r] += 1
                    else:
                        # if false: just add it with 1 (first step)
                        tempDic[r] = 1    
    # create list results
    results = []
    # loop through all items of the dictionry
    for k,v in tempDic.items():
        # string formatting (old style) - new: "{1:010d}\t{0}".format(k, v)
        result = "%010d\t%s" % (v, k)
        # appending the strings to the list
        results.append(result)

    # descending sort of the list
    results = sorted(results, reverse=True)
    # string created by joining the items of the list (separator \n)
    results = "\n".join(results)

    # create or open file bibtex_analysis.txt
    with open("bibtex_analysis.txt", "w", encoding="utf8") as f9:
        # write results
        f9.write(results)

# call the function bibAnalyze with the filename as input value
bibAnalyze(vars['bib_all'])



