#! /usr/bin/env python3

import json
with open('jsonExample.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    for element in jsonObject:
        #print(str(element) + "\n")
        for subElement in element:
            print("key = " + str(subElement) + "  ---  " + "value = " + str(element[subElement]) + "\n")
        print("\n**************************\n")

