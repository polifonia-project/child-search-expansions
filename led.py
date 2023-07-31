def doQuery(query):
    return ""


def getSampleResults():
    with open("sample-results.txt", 'r') as file:
        text = file.read()
    return text


def generateSPARQLQueryFromTerms(termsDict):
    queryChunks = []
    for term in termsDict:
        tempList = []
        tempList.append(term)
        for synonym in termsDict[term]:
            tempList.append(synonym)
        tempString = ' '.join(tempList)
        withBracketsStr = '{ ?o bds:search \'' + tempString + '\' . ?s rdf:value ?o }'
        queryChunks.append(withBracketsStr)
    searchString = ' '.join(queryChunks)
    print(searchString)

    query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n" \
            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n" \
            "PREFIX led: <http://led.kmi.open.ac.uk/term/> \n" \
            "PREFIX dct: <http://purl.org/dc/terms/> \n" \
            "PREFIX pl: <http://purl.org/NET/c4dm/event.owl#> \n" \
            "PREFIX bds: <http://www.bigdata.com/rdf/search#> \n" \
            "SELECT ?s ?p ?o \n" \
            "FROM <http://data.open.ac.uk/context/led> \n" \
            "WHERE { \n" \
            "" + searchString + "\n" \
                                               "} \n" \
                                               "LIMIT 20"
    return query
