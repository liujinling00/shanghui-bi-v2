# -*- coding: utf-8 -*-
import json
import os

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'members.csv')

with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

headers = ['姓名','性别','年龄段','政治面貌','所属行业','区域','区县','会内职位','入会年份','会费状态','所属企业','好人好事']
field_keys = ['name','gender','ageGroup','politicalStatus','industry','region','district','position','joinYear','membershipStatus','company','goodDeeds']

lines = [','.join(headers)]
for m in data['members']:
    cells = []
    for k in field_keys:
        val = str(m.get(k, ''))
        val = val.replace('"', '""')
        cells.append('"' + val + '"')
    lines.append(','.join(cells))

with open(csv_path, 'w', encoding='utf-8-sig') as f:
    f.write('\n'.join(lines))

print('Generated members.csv with {} rows'.format(len(data['members'])))
print('File: {}'.format(csv_path))
