# Extraction-based Text Summariser 

Typical automatic text summarisation makes use of either an **extraction** or an **abstraction** based model. This project specifically is an implementation of a **feature-based extraction summariser**. _(While an additional abstraction layer was intended to be compounded with this summariser, as of now, it is only a purely extraction-based model.)_

Extraction methods work by selecting a subset of existing words, phrases, or sentences in the original text and concatenate them to form a summary. Extractive systems are quite robust since they use existing natural language phrases that are taken straight from the input. However, they lack in flexibility since they cannot use novel words or connectors.   

In contrast, abstraction methods build an internal semantic representation and then use natural language generation techniques to create a summary that is closer to what a human might express. Such a summary, while intended to keep the original content’s intent, can use words that were not in the original input. The primary goal of an abstractive model is to create more fluent and natural summaries. However, such a model constitutes a harder problem as we now require the model to generate coherent phrases and connectors.

Abstraction modelled summarisation is still a very heavily researched field, which is why most established automatic text summarisers make use of extraction models. Clustering of phrases and sentences in extraction-based summarisation make use of either a **graph-based**, **feature-based**, **topic-based**, or **grammar-based** systems.


## General Specs
* the entire source code is written in **Python 2.7** 
* change the source and target documents in docs/main.py as required

# Feature-based Summarisation
The feature-based model extracts the features of a sentence, then evaluates their importance. 

In any typical feature-based model, the following features are used: 
* Location of the sentence in the document
* Presence of various parts of speech like verbs
* Length
* Term frequency 
* Proper Nouns
* Formatting and styles 

A system is built to indicate references via pronouns to previous sentences and incorporated into the scoring mechanism. 

A score is granted to each sentence accordingly. The sentences that are ranked with this score, tend to be repetitive in nature, often talking about the same subject material. Hence, it is important to not include new sentences that refer to the same information. We intend to achieve this in the abstracting layer of the project. 

Another popular algorithm is the Luhn’s Algorithm which evaluates score based on frequency. However, we will not be using it owing to lack of multiple factors and a possibility that it wouldn’t work well with an abstraction layer.

---
**_Other extraction models_**

_Graph Based_
_A stochastic graph base model that computes the relative importance of text-units. It builds a graph from the document, with words as nodes and edges weighted according to relevance relations._
_TextRank is the typical graph-based method and is based on the infamous PageRank system used by Google Search Engines. Works on the principle that the more the links to a textual-unit the better it is. The weighted edges are represented by an adjacency matric. This is then converted into a transition probability matrix by taking total probability of the links for each textual-unit. A ‘PageSurfer’ accordingly iterates this transition until convergence below a threshold._ 
_TextRank regards words or sentences as pages on the PageRank. For the interests of this project, however, we will be using a LexRank. LexRank uses the sentence as node and the similarity as relation/weight (similarity is calculated by IDF-modified Cosine similarity)._

_Topic Based_
_The topic base model calculates the various topics of each document and then evaluates each sentence upon their reference to various topics and scores it accordingly. A priority order can be maintained in the topic list itself, thus paying more attention to sentences that refer to the important and recurrent themes of the document._ 
_Latent Semantic Analysis (LSA) will be used to the detect the topic. It is an algebraic-statistical method that extracts hidden semantic structures of words and sentences. It employs the Singular Value Decomposition (SVD) algorithm to find the inter-relation between various sentences and words._
