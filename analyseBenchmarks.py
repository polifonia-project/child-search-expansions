from chatgpt import *
from led import *
import re
import urllib.parse
import os
from flask import request
import json
import csv
import requests
import urllib.parse

# benchmark_file = 'data/benchmarkLEs.json'
# benchmark_file = 'data/sample1.json'
benchmark_file = 'data/all_lexp.json'

output_file = 'data/analysisResults3.json'
output_file_csv = 'data/analysisResults3.csv'
results = []

counter = 0
failed = 0

with open(benchmark_file, "r") as file:
    benchmarkDict = json.load(file)

for lexp in benchmarkDict:
    text = benchmarkDict[lexp]
    try:
        categorisationResult = json.loads(categoriseChildhood(text))
    except:
        failed = failed + 1
        print("Failed to categorise")
    singleResult = dict()
    singleResult['lexp'] = lexp
    singleResult['text'] = text
    singleResult['childhood'] = categorisationResult['childhood']
    singleResult['reason'] = categorisationResult['reason']
    results.append(singleResult)
    counter = counter + 1
    print("categorised items: " + str(counter), end='\r')


with open(output_file, 'w') as json_output:
    json_output.write(json.dumps(results, indent=4))

field_names = ['lexp', 'text', 'childhood', 'reason']

with open(output_file_csv, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(results)

print("**************************")
print("processed " + str(counter) + " items")
print("Failures: " + str(failed))


