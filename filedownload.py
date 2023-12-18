import requests
import os

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(), 'example1.txt')
r = requests.get(url)
if r.status_code == 200:
    with open(path, 'wb') as f:
        f.write(r.content)
    print("Download successful. File saved at:", path)
else:
    print("Failed to download. Status code:", r.status_code)
    print(r.content)
