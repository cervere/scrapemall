import os

DELIMITTER = ","
DATA_FILES_CSV = "./input-data/"
DATA_FILES_JSON = "./json-data/"
BATCH_SIZE = 1000
INDEX_NAME = "write-ads"
INDEX_TYPE = "ad"
#HEADER = '{ "index": { "_index": "'+INDEX_NAME+'", "_type": "'+INDEX_TYPE+'" } }'
HEADER = "channelId,channelName,adId,adUrl,adType,adSize,dateCreated,websiteId,website,category,subCategory"
FIELDS = HEADER.rstrip('\n').split(DELIMITTER)

def trimQuotes(str):
    str = str.rstrip('\n')
    if str.startswith('"') and str.endswith('"'):
        str = str[1:-1]
    return str

def getjsonrow(line):
    global FIELDS
    data = line.split(DELIMITTER)
    str = ''
    for i in range(len(FIELDS)):
        if i>0:
            str += ', '
        str += '"' + trimQuotes(FIELDS[i]) + '" : "' + trimQuotes(data[i]) + '"'
    return '{' + str + '}'

def flush(filenum, datastr, dateYMD='UNSPECIFIED'):
        datastr = '[' + datastr
        datastr = datastr[:-1] + ']'
        filename = DATA_FILES_JSON + '/' + dateYMD + '/' + 'data.' +str(filenum) + '.json'
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        datajson = open(filename, 'w') #Filename to be time specific
        datajson.write(datastr)
        datajson.close()
    
def prepareData():
    print "called"
    file = open(DATA_FILES_CSV + "Ad_Export.csv", 'r')
    header = next(file)
    print header
    global FIELDS
    FIELDS = header.rstrip('\n').split(DELIMITTER)
    datastr = ''
    lines=0
    for line in file:
        datastr += "\n" + getjsonrow(line)+ "," 
        lines+=1
        if (lines % BATCH_SIZE) == 0:
            flush((lines/BATCH_SIZE), datastr)
            datastr = ''
    flush((lines/BATCH_SIZE)+1, datastr)
