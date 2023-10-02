import openai
import json
from config import *

openai.api_key = getOpenaiKey()

def keywordExpansion(inputTerms):
    messages = [
        # {"role": "system", "content": "You are a helpful search assistant that can provide information."},
        {"role": "user", "content": "Expand each of the terms listed below into synonyms and related terms. "
                                    "Create exactly 15 of them. Display the "
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


def categoriseChildhood(lexp):
    messages = [
        # {"role": "system", "content": "You are a helpful search assistant that can provide information."},
        # {"role": "user", "content": "Does the following passage describe childhood experiences of listening to music?"
        #                            "Give me the answer as a JSON structure with two keys: 'childhood' and 'reason'. The attribute "
        #                            "of 'childhood' should either be true or false and the attribute of 'reason' should be the reasons for you answer."},

        {"role": "user", "content": "Does the following passage cover the theme of childhood/youth or describe or mention childhood/youth or children and young people in any way?"
                                    "Give me the answer as a JSON structure with two keys: 'childhood' and 'reason'. The attribute "
                                    "of 'childhood' should either be true or false and the attribute of 'reason' should be the reasons for you answer."},
        {"role": "user", "content": f"{lexp}"},
    ]
    finalResponse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        # engine=engine
    )
    return finalResponse["choices"][0]["message"]["content"]
