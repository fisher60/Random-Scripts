def remove_duplicate(a):
    return sorted([{'data': {'id': y}}for y in list(set([j['data']['id'] for j in a]))],key=lambda x:x['data']['id'])

Nodes=[
    {'data': {'id': 'A'}},
    {'data': {'id': 'A'}},
    {'data': {'id': 'A'}},
    {'data': {'id': 'A'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'D'}},
    {'data': {'id': 'D'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'E'}},
    {'data': {'id': 'E'}}]

print(remove_duplicate(Nodes))