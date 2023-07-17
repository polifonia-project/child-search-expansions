from chatgpt import *
from led import *
import re
from flask import *
import urllib.parse
import os
from flask import request

app = Flask(__name__, template_folder="templates", static_folder="static")

def run(input_request):
    search_query = generate_search_query(input_request)
    #return search_query

    print(f"Searching LED with: {search_query}")

    search_results = getSampleResults()

    if len(search_results) == 0:
        return "Not enough LED results"

    answer = generate_answer(input_request, search_results)
    # accept_header = request.headers.get('Accept')
    '''
    if accept_header and "json" in accept_header:
        return render_json_response(answer, search_results, titles, search_query)
    return render_response(answer, search_results, titles, search_query)
    '''
    return answer

def getQuery(input_request):
    search_query = generate_search_query(input_request)
    return search_query


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return ("Woooot! Success")

@app.route("/query")
def query():
    q = request.args.get("q")
    answer = getQuery(q)
    return answer

@app.route("/ask")
def ask():
    q = request.args.get("q")
    answer = run(q)
    return answer


if __name__ == "__main__":
    if os.getenv("debug"):
        app.run(debug=True)
    else:
        from waitress import serve

        serve(app, host="0.0.0.0", port=5005)
