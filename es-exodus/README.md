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

Test if DB connection works

```shell
$ python dbtest.py
Total results processed - 211
Total time for executing query - 478.649139404 ms
Total time for preparing data - 0.0748634338379 ms
```
 
