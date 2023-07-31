import openai
import json
from config import *

openai.api_key = getOpenaiKey()


# engine = "lxt-aimwa-dev-gpt4-us"


def generate_search_query(input_request):
    messages = [
        # {"role": "system", "content": "You are a helpful search assistant that can provide information."},
        {
            "role": "user",
            "content": "Generate a valid SPARQL query to search a knowledge graph of historical listening "
                                    "experiences that answers the question. Prioritize the most important keywords and "
                                    "add synonyms to focus the search. Ensure that the response contain only the query and no other extra text. "
                                    "A search for the term 'childhood' is shown below. Use this as a template for the query:"
                                    """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX led: <http://led.kmi.open.ac.uk/term/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX pl: <http://purl.org/NET/c4dm/event.owl#>
PREFIX bds: <http://www.bigdata.com/rdf/search#>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

select ?s ?p ?o
FROM <http://data.open.ac.uk/context/led>
WHERE {
 ?o bds:search "childhood" .
 ?s rdf:value ?o
}
                                    """},
        {"role": "user", "content": f"{input_request}"},
        # {"role": "user", "content": "Show me children's experiences of listening to music"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["message"]["content"].replace("\"", "").replace(":", "")


def generate_answer(input_request, search_results):
    global final_answer
    messages = [
        {"role": "system", "content": "You are a helpful search assistant that can provide information."},
        {"role": "user", "content": "Generate a comprehensive answer (but no more than 160 words) for the "
                                    "question based solely on the search results given. You must only use "
                                    "information from the provided search results. Use an unbiased and journalistic "
                                    "tone. Combine search results together into a coherent answer. Do not repeat text."},
        {"role": "user", "content": f"{input_request}"},
        # {"role": "assistant", "content": f"{json.dumps(search_results)}"}
        {"role": "assistant", "content": f"{search_results}"}
    ]

    print(messages)
    finalResponse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        # engine=engine
    )
    return finalResponse["choices"][0]["message"]["content"]

def keywordExpansion (inputTerms):
    messages = [
        # {"role": "system", "content": "You are a helpful search assistant that can provide information."},
        {"role": "user", "content": "Expand each of the terms listed below into synonyms and related terms. "
                                    "Only use single words for the related terms or synonyms. Display the "
                                    "new terms in a JSON structure with the original terms as a key and "
                                    "the list of terms as an array attribute."},
        {"role": "user", "content": f"{inputTerms}"},
    ]
    finalResponse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        # engine=engine
    )
    return finalResponse["choices"][0]["message"]["content"]

