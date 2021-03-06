from datetime import datetime
from pyelasticsearch import ElasticSearch
from dbconnect import *

import argparse
import json
import os

es = ElasticSearch()

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--date", required = True, help = "date to index")
args = vars(ap.parse_args())


ad_mapping = {
    'ad': {
        'properties': {
            'channelId': {'type': 'integer'},
            'channelName': {'type': 'string'},
            'adId': {'type': 'integer'},
            'adUrl': {'type': 'string'},
            'adType': {'type': 'string'},
            'adSize': {'type': 'string'},
            'dateCreated': {'type': 'date', 'format' : 'YYYY-MM-dd HH:mm:ss'},
            'websiteId': {'type': 'integer'},
            'website': {'type': 'string', 'analyzer': 'simple'},
            'category': {'type': 'string'},
            'subCategory': {'type': 'string'}
        }
    }
}


es.health(wait_for_status='yellow')
es.delete_index('write-ads')
es.create_index('write-ads', settings={'mappings': ad_mapping})

dateYMD = args["date"]
prepareDataFromDB(dateYMD)

dir = DATA_FILES_JSON + '/' + dateYMD
for filename in os.listdir(dir):
    if filename.endswith('.json'):
        with open(dir + '/' + filename) as open_file:
            json_docs = json.load(open_file)
            es.bulk((es.index_op(doc) for doc in json_docs),
                index='write-ads',
                doc_type='ad')

es.refresh("write-ads")

res = es.search('website:com', index='write-ads')
print("Got %d Hits for .com websites" % res['hits']['total'])
for hit in res['hits']['hits']:
    print (hit["_source"])
res = es.search('website:in', index='write-ads')
print("Got %d Hits for .in websites" % res['hits']['total'])
res = es.search('category:entertainment', index='write-ads')
print("Got %d Hits for category:Entertainment" % res['hits']['total'])
