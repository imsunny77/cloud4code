data= [
        {"camp":1,"bid":1},
        {"camp":1,"bid":2},
        {"camp":2,"bid":3},
        {"camp":2,"bid":4},
        {"camp":3,"bid":5}
    ]
new_list = list()
for dict in data:
    if new_list==[]:
        new_list.append(dict)
    else:
        for dict2 in new_list:
            if dict2['camp'] == dict['camp']:
                temp = {'bid':[dict2['bid'],dict['bid']]}
                dict2.update(temp)
        if not any(d['camp'] == dict['camp'] for d in new_list):
            new_list.append(dict)

print(new_list)
# [{'camp': 1, 'bid': [1, 2]}, {'camp': 2, 'bid': [3, 4]}, {'camp': 3, 'bid': 5}]
