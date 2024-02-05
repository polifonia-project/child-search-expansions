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
        # model="gpt-3.5-turbo",
        model="gpt-4-1106-preview",
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
                                    "of 'childhood' should either be true or false and the attribute of 'reason' should be the reasons "
                                    "for you answer. Please do not include any artifacts for formatting. Just give me the "
                                    "JSON object and nothing else."},
        {"role": "user", "content": f"{lexp}"},
    ]
    finalResponse = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model="gpt-4-1106-preview",
        response_format = {
            "type": "json_object"
        },
        messages=messages,
        # engine=engine
    )
    # print("******FULL RESPONSE*******")
    # print(finalResponse)
    # print("******FULL RESPONSE END*******")
    return finalResponse["choices"][0]["message"]["content"]

def categoriseChildhoodScenario(lexp):
    lexp = "Passage: " + lexp
    scenario = "Scenario: Ortenz wants to characterize children’s experience of music as witnessed in bibliographic " \
               "and artistic sources. She is looking for primary sources (e.g. Personal journals, literary texts) " \
               "wherein to find evidence of listening experiences. She needs to collect and analyze large corpora " \
               "of texts and images recording or depicting children’s experience with music. Documents include " \
               "official sources (e.g. newspaper articles, reviews of concerts, paintings) and sources produced by 'odinary people'. " \
               "She prefers the latter as they provide more reliable feedback, and she looks at the context of " \
               "production of such sources (where, when, who created the source, the goal, which related events exist), " \
               "contents (recurring motifs and themes), and elicited emotional responses. She collects sources " \
               "belonging to different historical periods so as to characterize the development of identified phenomena."
    messages = [
        # {"role": "system", "content": "You are a helpful search assistant that can provide information."},
        # {"role": "user", "content": "Does the following passage describe childhood experiences of listening to music?"
        #                            "Give me the answer as a JSON structure with two keys: 'childhood' and 'reason'. The attribute "
        #                            "of 'childhood' should either be true or false and the attribute of 'reason' should be the reasons for you answer."},

        {"role": "user", "content": "Does the following passage help address and answer the scenario described below?"
                                    "Give me the answer as a JSON structure with two keys: 'childhood' and 'reason'. The attribute "
                                    "of 'childhood' should either be true or false to indicate your answer and the attribute of 'reason' should "
                                    "be the reasons for you answer. Please do not include any artifacts for formatting. "
                                    "Just give me the JSON object and nothing else."},
        {"role": "user", "content": f"{scenario}"},
        {"role": "user", "content": f"{lexp}"},
    ]
    finalResponse = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model="gpt-4-1106-preview",
        response_format={
            "type": "json_object"
        },
        messages=messages,
        # engine=engine
    )
    # print("******FULL RESPONSE*******")
    # print(finalResponse)
    # print("******FULL RESPONSE END*******")
    return finalResponse["choices"][0]["message"]["content"]
