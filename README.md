---
component-id: child-search-expansion
type: Software
name: CHILD Search expansion using LLMs
description: This software component was developed with the aim of supporting the identification of implicit themes in text and takes as reference the documentary evidence benchmark
work-package: 
  - WP4
pilot:
  - CHILD
project: polifonia-project
resource: https://github.com/polifonia-project/child-search-expansions/
release-date: 05/09/2023
release-number: v0.1
release-link: https://github.com/polifonia-project/child-search-expansions/releases/tag/v0.1
doi: https://zenodo.org/badge/latestdoi/588597123
changelog: https://github.com/polifonia-project/child-search-expansions/releases/tag/v0.1
licence:
  - Apache-2.0
copyright: "Copyright (c) 2023 CHILD @ The Open University"
contributors:
  - Jason Carvalho <https://github.com/JaseMK>
  - Alba Morales Tirado <https://github.com/albamoralest>
  - Enrico Daga <https://github.com/enridaga>
credits:
  - https://github.com/JaseMK
  - https://github.com/albamoralest
  - https://github.com/enridaga
---

# CHILD - Search expansion using LLMs

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8322490.svg)](https://doi.org/10.5281/zenodo.8322490)


This software component was developed with the aim of supporting the identification of 
implicit themes in text and takes as reference the documentary evidence benchmark.

Interactions with the ChatGPT API (or other LLM) is currently handled in 
the `chatgpt.py` file. Interactions with the LED knowledge graph are handled in `led.py`. In 
order to run any of the scripts in this distribution, a copy of `config.py.dist` must be 
made, called `config.py`, in which a valid OpenAI API key should be specified.

`runTest.py` can be used to run the keyword expansion and test the results in a SPARQL 
query issued against a knowledge graph. The returned results (a list of 
listening experiences) are stored in `output/output.txt`. These results can 
be analysed for precision and recall values against the documentary evidence benchmark 
data by running `precisionRecall.py`.


