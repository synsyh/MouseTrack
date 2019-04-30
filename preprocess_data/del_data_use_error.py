import json

with open('error.txt') as f:
    del_id_list = {}
    for line in f.readlines():
        line = line.strip()
        tmp = line.split('-')
        if len(tmp) == 2:
            id = tmp[0]
            chars = tmp[1]
            del_id_list[id] = chars
        elif len(tmp) == 1:
            del_id_list[tmp[0]] = ''
with open('error_drawers.json') as f:
    data = f.read()
data = json.loads(data)
print()
for id, chars in del_id_list.items():
    if id not in data.keys():
        print(id)
        continue
    if chars == '':
        data.pop(id)
    for char in chars:
        data[id].pop(char)
for drawer, paths in data.items():
    try:
        data[drawer].pop('i')
        data[drawer].pop('I')
        data[drawer].pop('l')
    except KeyError:
        continue
with open('drawers.json', 'w') as f:
    f.write(json.dumps(data, indent=4))
