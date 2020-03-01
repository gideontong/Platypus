import requests, json, re
from datetime import datetime

targetFile = open('targets.json')
targetData = json.load(targetFile)

endpoint = "https://access.redhat.com/hydra/rest/securitydata/cve.json"
cveUri = "https://access.redhat.com/hydra/rest/securitydata/cve/"

payload = {}
headers = {}

for target in targetData:
    url = endpoint + "?" + "package=" + target
    responseData = requests.request("GET", url, headers=headers, data = payload)
    response = json.loads(responseData.text)
    with open('target_' + target + '.json', 'w') as outfile:
        json.dump(response, outfile)
    cveData = {}
    size = len(response)
    i = 0
    for CVE in response:
        i += 1
        if CVE['severity'] == 'low':
            continue
        cveEndpoint = cveUri + CVE['CVE'] + ".json"
        cveResponseData = requests.request("GET", cveEndpoint, headers=headers, data = payload)
        cveResponse = json.loads(cveResponseData.text)
        # print(cveResponse)
        print("[", datetime.now(), "]", i, "/", size, CVE['CVE'])
        if 'affected_release' not in cveResponse:
            continue
        try:
            for release in cveResponse['affected_release']:
                if target not in release['package']:
                    continue
                versionMatch = re.search('[0-9]*\.[0-9]*', release['package'])
                # print(versionMatch)
                # print(release)
                # print(release['package'])
                version = versionMatch.group()
                # print(version)
                if version not in cveData:
                    cveData[version] = []
                if CVE['CVE'] not in cveData[version]:
                    # print(cveData[version])
                    major = ""
                    for detail in cveResponse['details']:
                        major += " " + detail
                    cveData[version].append(CVE['CVE'])
        except:
            pass
    # with open('target_' + target + '_cve_backup.txt', 'w') as outfile:
        # outfile.write(str(cveData))
    with open('target_' + target + '_cve.json', 'w') as outfile:
        json.dump(cveData, outfile)
