import json

json.dump({"City" : "Sylhet", "Country" : "Bangladesh" },open('data.json','w'))
print(json.load(open('data.json')))
