import urllib.request, base64, ssl, json, sys, getpass, time

siteUrl = sys.argv[1]
username = sys.argv[2]
password = getpass.getpass("Jira password: ")
filterId = sys.argv[3]
output = sys.argv[4]

# fields: key, created, priority, status

def request(url):
    base64str = base64.b64encode(("%s:%s" % (username, password)).encode()).decode("ascii")
    headers = { "Authorization" : "Basic %s" % base64str }
    request = urllib.request.Request(url, headers=headers)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    response = urllib.request.urlopen(request, context=gcontext)
    encodedJson = response.read()
    decodedJson = encodedJson.decode("utf-8")
    return json.loads(decodedJson)

def getFilter(id):
    url = "%s/rest/api/2/filter/%s" % (siteUrl, id)
    return request(url)

def search(filterId):
    url = "%s&fields=key,created,priority,status" % getSearchUrlByFilter(filterId)
    return request(url)

def getSearchUrlByFilter(filterId):
    filter = getFilter(filterId)
    print(filter)
    return filter["searchUrl"]

def jsonIssuesListToCsv(issuesList):
    parsedIssueList = ['sep=,',str(len(issuesList["issues"]))]
    for issue in issuesList["issues"]:
        parsedIssueList.append("%s,%s,%s,%s" % (issue["key"], issue["fields"]["created"], issue["fields"]["priority"]["name"], issue["fields"]["status"]["name"]))

    return "\n".join(parsedIssueList)

f = open(output, 'w')
outputText = jsonIssuesListToCsv(search(filterId))
print(outputText)
f.write(outputText)
f.close()
    
    
