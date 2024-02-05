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
import time

# benchmark_file = 'data/benchmarkLEs.json'
# benchmark_file = 'data/sample1.json'
benchmark_file = 'data/all_lexp.json'

output_file = 'data/analysisResults_child_gpt4-2.json'
output_file_csv = 'data/analysisResults_child_gpt4-2.csv'
results = []

counter = 0
failed = 0

# TIMER INFO FOR RATE LIMITING
# the maximum number of iterations per minute
max_iter = 20
# define the minimum time interval between iterations in seconds
min_interval = 60 / max_iter
# initialize a variable to store the start time of the loop
start_time = time.time()


# create an empty array to store the strings
stringsToTest = []

# open the text file in read mode
with open("data/evaluationLEs.csv", "r") as file:
    # loop through each line in the file
    for line in file:
        # strip the newline character from the line
        line = line.strip()
        # append the line to the array
        stringsToTest.append(line)

with open(benchmark_file, "r") as file:
    benchmarkDict = json.load(file)

for lexp in benchmarkDict:
    text = benchmarkDict[lexp]
    # Process all items (if True) or process just a selection in the stringsToTest array
    # if True:
    if lexp in stringsToTest:
        try:
            chatGptOutput = categoriseChildhood(text)
            # print(chatGptOutput)
            categorisationResult = json.loads(chatGptOutput)
            # categorisationResult = json.loads(categoriseChildhoodScenario(text))
        except Exception as e:
            print(e)
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
        # calculate the elapsed time since the start of the loop
        elapsed_time = time.time() - start_time
        # calculate the average time per iteration
        avg_time = elapsed_time / counter
        # check if the average time is less than the minimum interval
        if avg_time < min_interval:
            # calculate the time to wait before the next iteration
            wait_time = min_interval - avg_time
            # sleep for the wait time
            time.sleep(wait_time)
    if counter >= 200:
        break


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


