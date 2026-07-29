# -*- coding: utf-8 -*-
import json
import random
import os

random.seed(42)

industries = ['制造业','房地产','建筑工程','科技互联网','金融投资','商贸物流','餐饮服务','教育培训','医疗健康','文化传媒','农业科技','新能源']
regions = ['沈阳市','大连市','鞍山市','抚顺市','本溪市','锦州市','营口市','辽阳市','盘锦市','铁岭市']
districts = ['和平区','沈河区','大东区','皇姑区','铁西区','浑南区','于洪区','沈北新区','苏家屯区','辽中区']
political = ['中共党员','共青团员','群众','民主党派']
age_groups = ['25-30岁','31-35岁','36-40岁','41-45岁','46-50岁','51-55岁']
surnames = ['王','李','张','刘','陈','杨','赵','黄','周','吴','徐','孙','胡','朱','高','林','何','郭','马','罗']
given_names = ['伟','芳','娜','敏','静','丽','强','磊','军','洋','勇','艳','杰','娟','涛','明','超','霞','平','刚','玲','丹','萍','鹏','华','彬','宇','晨','雪','慧']

def pick(arr):
    return random.choice(arr)

def pick_w(arr, weights):
    total = sum(weights)
    r = random.random() * total
    for i in range(len(arr)):
        r -= weights[i]
        if r <= 0:
            return arr[i]
    return arr[-1]

members = []
mid = 1

# 会长
members.append({
    'id': mid, 'name': pick(surnames)+'志远', 'gender': '男', 'ageGroup': '46-50岁',
    'politicalStatus': '中共党员', 'industry': pick(industries), 'region': '沈阳市',
    'district': pick(districts), 'position': '会长', 'joinYear': 2018, 'goodDeeds': 5,
    'membershipStatus': '在籍', 'company': '远东集团'
})
mid += 1

# 副会长 x12
for _ in range(12):
    members.append({
        'id': mid, 'name': pick(surnames)+pick(given_names),
        'gender': '男' if random.random() > 0.2 else '女',
        'ageGroup': pick_w(age_groups, [1,3,5,4,3,2]),
        'politicalStatus': pick_w(political, [4,1,3,2]),
        'industry': pick(industries),
        'region': pick_w(regions, [5,3,1,1,1,1,1,1,1,1]),
        'district': pick(districts), 'position': '副会长',
        'joinYear': 2018 + random.randint(0, 3),
        'goodDeeds': random.randint(0, 3), 'membershipStatus': '在籍',
        'company': pick(industries).replace('业','')+'有限公司'
    })
    mid += 1

# 理事 x35
for _ in range(35):
    members.append({
        'id': mid, 'name': pick(surnames)+pick(given_names),
        'gender': '男' if random.random() > 0.3 else '女',
        'ageGroup': pick_w(age_groups, [2,4,5,4,2,1]),
        'politicalStatus': pick_w(political, [3,2,4,1]),
        'industry': pick(industries),
        'region': pick_w(regions, [5,3,1,1,1,1,1,1,1,1]),
        'district': pick(districts), 'position': '理事',
        'joinYear': 2018 + random.randint(0, 5),
        'goodDeeds': random.randint(0, 2),
        'membershipStatus': '在籍' if random.random() > 0.05 else '未缴费',
        'company': pick(industries).replace('业','')+'有限公司'
    })
    mid += 1

# 会员 x270
for _ in range(270):
    members.append({
        'id': mid, 'name': pick(surnames)+pick(given_names),
        'gender': '男' if random.random() > 0.35 else '女',
        'ageGroup': pick_w(age_groups, [3,5,4,3,2,1]),
        'politicalStatus': pick_w(political, [2,2,5,1]),
        'industry': pick(industries),
        'region': pick_w(regions, [4,3,1,1,1,1,1,1,1,1]),
        'district': pick(districts), 'position': '会员',
        'joinYear': 2018 + random.randint(0, 7),
        'goodDeeds': random.randint(0, 1),
        'membershipStatus': '在籍' if random.random() > 0.1 else '未缴费',
        'company': pick(industries).replace('业','')+'有限公司'
    })
    mid += 1

data = {
    'meta': {
        'title': '沈阳市年轻一代民营企业家商会',
        'subtitle': 'BI 智能看板',
        'lastUpdate': '2026-07-29',
        'version': '2.0',
        'description': '商会会员数据分析与可视化平台'
    },
    'members': members
}

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, 'data.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

male = sum(1 for m in members if m['gender'] == '男')
female = sum(1 for m in members if m['gender'] == '女')
active = sum(1 for m in members if m['membershipStatus'] == '在籍')
print(f'Generated {len(members)} members to {out_path}')
print(f'Male: {male}, Female: {female}')
print(f'In good standing: {active}')
print(f'Positions: 会长={sum(1 for m in members if m["position"]=="会长")}, 副会长={sum(1 for m in members if m["position"]=="副会长")}, 理事={sum(1 for m in members if m["position"]=="理事")}, 会员={sum(1 for m in members if m["position"]=="会员")}')
