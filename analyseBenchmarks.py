from chatgpt import *
from led import *
import re
import urllib.parse
import os
from flask import request
import json
import requests
import urllib.parse

benchmark_file = 'data/benchmarkLEs.json'
output_file = 'data/analysisResults.json'
resultsDict = dict()

with open(benchmark_file, "r") as file:
    benchmarkDict = json.load(file)

for lexp in benchmarkDict:
    text = benchmarkDict[lexp]
    singleResult = json.loads(categoriseChildhood(text))
    singleResult['text'] = text
    resultsDict[lexp] = singleResult

with open(output_file, 'w') as json_output:
    json_output.write(json.dumps(resultsDict, indent=4))


