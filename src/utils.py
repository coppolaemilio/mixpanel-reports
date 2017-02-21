import json
from operator import itemgetter
import collections
import urlparse

def count_and_order(property, url_key):
    file = []
    for line in open('data/file.json', 'r'):
        file.append(json.loads(line))

    marketing_key_list = []
    for i in file:
        question = i.get('properties').get(property)
        value = ''
        if question:
            if url_key in question:
                parsed = urlparse.urlparse(question)
                value = urlparse.parse_qs(parsed.query)[url_key]
                if value != '':
                    marketing_key_list.append(value[0])



    counted = collections.Counter(marketing_key_list)
    counted = collections.OrderedDict(counted.most_common())
    for i in counted.keys():
        print str(i) + ": " + str(counted[i])