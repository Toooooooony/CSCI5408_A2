from elasticsearch import helpers, Elasticsearch
import csv
import certifi
import json

es = Elasticsearch(
    ['https://portal-ssl1525-28.bmix-dal-yp-c3a5bfc4-f275-4e43-8650-5d2e30539e61.2991161829.composedb.com:57500'],
    http_auth=('admin', 'GREQJGHGFDXJJAXZ'),
    scheme="https",
    port=57500,
)

data = []

with open('tweets_result.csv',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='tweets_result', doc_type='TYPE')


print("Done!")
