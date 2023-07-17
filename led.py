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
        tempString = ' OR '.join(tempList)
        withBracketsStr = '(' + tempString + ')'
        queryChunks.append(withBracketsStr)
    searchString = ' AND '.join(queryChunks)
    print(searchString)

    query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " \
            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " \
            "PREFIX led: <http://led.kmi.open.ac.uk/term/> " \
            "PREFIX dct: <http://purl.org/dc/terms/> " \
            "PREFIX pl: <http://purl.org/NET/c4dm/event.owl#> " \
            "PREFIX bds: <http://www.bigdata.com/rdf/search#> " \
            "SELECT ?s ?p ?o " \
            "FROM <http://data.open.ac.uk/context/led> " \
            "WHERE { " \
            "?o bds:search '" + searchString + "' ." \
            "?s rdf:value ?o " \
            "}"
    return query
