DELIMITTER = ","
DATA_FILES_CSV = "./input-data/"
DATA_FILES_JSON = "./json-data/"
BATCH_SIZE = 1000
INDEX_NAME = "write-ads"
INDEX_TYPE = "ad"
HEADER = '{ "index": { "_index": "'+INDEX_NAME+'", "_type": "'+INDEX_TYPE+'" } }'

def trimQuotes(str):
    str = str.rstrip('\n')
    if str.startswith('"') and str.endswith('"'):
        str = str[1:-1]
    return str

def getjsonrow(line):
    global fields
    data = line.split(DELIMITTER)
    str = ''
    for i in range(len(fields)):
        if i>0:
            str += ', '
        str += '"' + trimQuotes(fields[i]) + '" : "' + trimQuotes(data[i]) + '"'
    return '{' + str + '}'

def flush(filenum, datastr):
        datastr = '[' + datastr
        datastr = datastr[:-1] + ']'
        datajson = open(DATA_FILES_JSON+'data.'+str(filenum)+'.json', 'w') #Filename to be time specific
        datajson.write(datastr)
        datajson.close()
    
def prepareData():
    file = open(DATA_FILES_CSV + "Ad_Export.csv", 'r')
    header = next(file)
    global fields 
    fields = header.rstrip('\n').split(DELIMITTER)
    datastr = ''
    lines=0
    for line in file:
        datastr += "\n" + getjsonrow(line)+ "," 
        lines+=1
        if (lines % BATCH_SIZE) == 0:
            flush((lines/BATCH_SIZE), datastr)
            datastr = ''
    flush((lines/BATCH_SIZE)+1, datastr)
