from chatgpt import *
from led import *
import re
from flask import *
import urllib.parse
import os
from flask import request
import json

input = 'childhood'

gptResponse = keywordExpansion(input)
print(gptResponse)
responseObj = json.loads(gptResponse)
query = generateSPARQLQueryFromTerms2(responseObj)
print (query)