import re
import yaml
import os
import shutil

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "config.yml"
settings = yaml.load(open(settingsFile), Loader=yaml.FullLoader)
bibKeys = yaml.load(open("zotero-bibliography-keys.yml"), Loader=yaml.FullLoader)

###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(records):

    bibDic = {}
    
    for record in records[1:]:
        if ".pdf" in record.lower():

            record = record.strip().split("\n")[:-1]

            rType = record[0].split("{")[0].strip()
            rCite = record[0].split("{")[1].strip().replace(",", "")

            bibDic[rCite] = {}
            bibDic[rCite]["rCite"] = rCite
            bibDic[rCite]["rType"] = rType

            for r in record[1:]:
                key = r.split("=")[0].strip()
                val = r.split("=")[1].strip()
                
                val = re.sub(r"\{|\},?", "", val)

                fixedKey = bibKeys[key]

                bibDic[rCite][fixedKey] = val
    
    return(bibDic)

def singleBib(records, key):
    i = 0
    for record in records[1:]:
        i += 1
        if key in record:
            result = "\n@" + records[i]
            return result

def makeStrucure():

    with open(settings["bib_all"], "r", encoding="utf8") as f1:
        records = f1.read().split("\n@")
    
    bibDic = bibLoad(records)
    
    for key in bibDic:
        subsubfolder = bibDic[key]["rCite"]
        subfolder = subsubfolder.lower()[:2]
        folder = subfolder[:1]

        mypath = os.path.join(settings["memex-path"], folder, subfolder, subsubfolder)
        
        if not os.path.exists(mypath):
            os.makedirs(mypath)

        mypathBib = mypath + "/" + subsubfolder + ".bib"

        with open(mypathBib, "w") as f2:
            f2.writelines(singleBib(records, key))

        mypathPdf = mypath + "/" + subsubfolder + ".pdf"

        if not os.path.isfile(mypathPdf):
            shutil.copyfile(bibDic[key]["file"], mypathPdf)
    
###########################################################
# RUN EVERYTHING ##########################################
###########################################################

makeStrucure()

print("Done!")