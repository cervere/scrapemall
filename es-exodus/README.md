#Database and Index
Python needs MySQLdb module to connect to DB. Make sure the module is installed.

If Db is not able to connect to DB, you see some error like this :

```shell
$ python dbtest.py
Traceback (most recent call last):
  File "dbtest.py", line 2, in <module>
    import MySQLdb
ImportError: No module named MySQLdb
```

First, install the required libraries:

```shell
$ apt-get install python-dev libmysqlclient-dev
```

Then, install the module :

```shell
$ pip install MySQL-python
```

Test if DB connection works. The query should give some results like this:

```shell
$ python dbtest.py
Total results processed - 211
Total time for executing query - 478.649139404 ms
Total time for preparing data - 0.0748634338379 ms
```
 
Once the DB connection is successful, run the *indexer* with a required (-d | --date) parameter in YYYY-MM-DD format:

```shell
$ python indexer.py -d 2015-09-20
Total results processed - 211
Total time for executing query - 756.687879562 ms
Total time for preparing data - 6.57200813293 ms
Got 177 Hits for .com websites
{u'website': u'SiliconIndia.com', u'category': u'News', u'adSize': u'300 X 105', u'subCategory': u'None', u'channelId': u'1', u'dateCreated': u'2015-09-20 03:18:58', u'adId': u'133', u'adType': u'jpeg', u'websiteId': u'41', u'channelName': u'Online', u'adUrl': u'https://drive.google.com/open?id=0BwhfKpveNm95Y2dSMHJxNzhwWkU'}
{u'website': u'SiliconIndia.com', u'category': u'News', u'adSize': u'108 X 76', u'subCategory': u'None', u'channelId': u'1', u'dateCreated': u'2015-09-20 03:18:58', u'adId': u'147', u'adType': u'jpeg', u'websiteId': u'41', u'channelName': u'Online', u'adUrl': u'https://drive.google.com/open?id=0BwhfKpveNm95SzJsSGVKUWdabmc'}
...
Got 21 Hits for .in websites
Got 39 Hits for category:Entertainment
```
