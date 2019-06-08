from featureExtractor import Summarize


title = 'random title'

file = open("docs/doc-birds.txt", "r")
text = file.read()

summaries = Summarize(title, text)
# print summaries

with open('docs/featureSummary.txt', 'w') as wr:
    for i, j in enumerate(summaries):
        wr.write(summaries[i] + '\n')
    wr.close()

print 'Summary extraction done!'