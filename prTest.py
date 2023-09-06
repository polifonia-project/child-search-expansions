from chatgpt import *
from led import *
import re
import urllib.parse
import os
from flask import request
import json
import requests
import urllib.parse

def write_strings_to_file(strings, file_name):
    try:
        with open(file_name, 'w') as file:
            for string in strings:
                file.write(string + '\n')
        print(f'Successfully wrote {len(strings)} strings to {file_name}.')
    except Exception as e:
        print(f'Error: {e}')

input = 'childhood'

# sparqlEndpoint = 'https://data.open.ac.uk/sparql'
sparqlEndpoint = 'http://localhost:9999/blazegraph/namespace/led'


headers = {
    'Accept': 'application/sparql-results+json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

gptResponse = keywordExpansion(input)
print(gptResponse)
gptResponseObj = json.loads(gptResponse)
query = generateSPARQLQueryFromTerms2(gptResponseObj)
print(query)
safeQuery = urllib.parse.quote_plus(query)
payload = 'query=' + safeQuery
ledResponse = requests.request("POST", sparqlEndpoint, headers=headers, data=payload)
# print(ledResponse.text)
ledResponseObj = ledResponse.json()
ledEntries = []
for item in ledResponseObj['results']['bindings']:
    print(item['excerpt']['value'])
    print(item['lexp']['value'])
    print(item['text']['value'])
    print('---------')
    ledEntries.append(item['lexp']['value'])

file_name = "output/output.txt"
write_strings_to_file(ledEntries, file_name)
