#!/usr/bin/python
import MySQLdb
import time
from preparedata import *

db = MySQLdb.connect(host="exodus.cyn9qtdt4hb5.us-west-2.rds.amazonaws.com", # your host, usually localhost
                     user="exodusapp", # your username
                      passwd="exodus123", # your password
                      db="exodus") # name of the data base

BATCH_SIZE = 1000
cur = db.cursor() 

base_query = """SELECT  
    cr.ChannelID channelId, 
    ch.Type channelName, 
    ad.ID adId, 
    ad.URL adUrl, 
    ad.Type adType, 
    ad.Size adSize, 
    cr.CreatedDateTime dateCreated, 
    we.ID websiteId, 
    we.URL website, 
    we.category category, 
    we.SubCategory subCategory 
    FROM 
    Crawl cr INNER JOIN Channel ch INNER JOIN Ad ad INNER JOIN Website we 
    ON 
    cr.ChannelID = ch.ID and cr.AdID = ad.ID and cr.WebsiteID = we.ID 
    ORDER by dateCreated 
    LIMIT """ 

processed = 0

ex = 0
prepare = 0

totresults = 0
while(True):
    #batch_query = base_query + str(processed) + "," + str(BATCH_SIZE)
    batch_query = base_query + str(1000) 

    a = time.time()
    cur.execute(batch_query)
    ex += (time.time() - a)

    results = 0

    b = time.time()
    for row in cur.fetchall() :
        #print DELIMITTER.join(str(x) for x in row)
        results += 1
    prepare += (time.time() - b)

    totresults += results
    break;

    processed += BATCH_SIZE


print "Total results processed - %d" % totresults
print "Total time for executing query - %s ms" % str(ex*1000)
print "Total time for preparing data - %s ms" % str(prepare*1000)


