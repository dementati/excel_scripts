import urllib.request, base64, ssl, json, sys, getpass, time

siteUrl = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
filterId = sys.argv[4]
output = sys.argv[5]
logFilename = sys.argv[6]

# fields: key, created, priority, status

logFile = None

def request(url):
    unit = "retrieveFilters.request"

    log(unit, "Sending request %s" % url)

    base64str = base64.b64encode(("%s:%s" % (username, password)).encode()).decode("ascii")
    headers = { "Authorization" : "Basic %s" % base64str }
    request = urllib.request.Request(url, headers=headers)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    response = urllib.request.urlopen(request, context=gcontext)
    encodedJson = response.read()

    log(unit, "Received response %s" % encodedJson)

    decodedJson = encodedJson.decode("utf-8")
    result = json.loads(decodedJson)

    log(unit, "Decoded and parsed as %s" % result)

    return result

def getFilter(id):
    unit = "retrieveFilters.getFilter"

    url = "%s/rest/api/2/filter/%s" % (siteUrl, id)

    log(unit, "Sending getFilter(id = %s)" % id)

    return request(url)

def search(filterId):
    unit = "retrieveFilters.search"

    url = "%s&fields=key,created,priority,status" % getSearchUrlByFilter(filterId)

    log(unit, "Sending search(filterId = %s)" % filterId)

    return request(url)

def getSearchUrlByFilter(filterId):
    unit = "retrieveFilters.getSearchUrlByFilter"

    filter = getFilter(filterId)
   
    log(unit, "Extracted search URL %s from filter ID %s" % (filter["searchUrl"], filterId))

    return filter["searchUrl"]

def jsonIssuesListToCsv(issuesList):
    parsedIssueList = ['sep=,',str(len(issuesList["issues"]))]
    for issue in issuesList["issues"]:
        parsedIssueList.append("%s,%s,%s,%s" % (issue["key"], issue["fields"]["created"], issue["fields"]["priority"]["name"], issue["fields"]["status"]["name"]))

    return "\n".join(parsedIssueList)

def log(unit, message):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    output = "[%s] %s: %s" % (now, unit, message)
    print(output)
    logFile.write("%s\n" % output)

def openLogFile(filename):
    global logFile
    logFile = open(filename, "a")

def closeLogFile():
    logFile.close()

unit = "retrieveFilters"

openLogFile(logFilename)
f = open(output, 'w')
outputText = jsonIssuesListToCsv(search(filterId))
log(unit, "Writing to output file: %s" % outputText)
f.write(outputText)
f.close()
closeLogFile()
    
    
