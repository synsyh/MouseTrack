import pymongo
import json

client = pymongo.MongoClient('mongodb://root:Koumin917@192.168.0.2:27017/')
db = client['collectpath']
col = db['collectpath']
drawers = {}
results = col.find({})
for result in results:
    drawer = result['IdentifyCode']
    if drawer in drawers.keys():
        if result['char'] in drawers[drawer]:
            drawers[drawer][result['char']].append(result['path'])
        else:
            drawers[drawer][result['char']] = [result['path']]
    else:
        trajs = {}
        trajs[result['char']] = [result['path']]
        drawers[drawer] = trajs
n_drawers = {}
for drawer, chars in drawers.items():
    if len(chars) != 52:
        continue
    else:
        flag = True
        for _, char in chars.items():
            if len(char) != 3:
                flag = False
                break
        if flag:
            n_drawers[drawer] = chars
with open('error_drawers.json', 'w') as f:
    f.write(json.dumps(n_drawers, indent=4))
