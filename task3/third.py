import json
import sys

with open(sys.argv[1], 'r') as f:
    tests_data = json.load(f)
with open(sys.argv[2], 'r') as f:
    values_data = json.load(f)
dict = {}
for item in values_data['values']:
    dict[item['id']] = item['value']

def put_values(tests):
    for test in tests:
        if test['id'] in dict:
            test['value'] = dict[test['id']]
        if 'values' in test:
            put_values(test['values'])

put_values(tests_data['tests'])
with open(sys.argv[3], 'w') as f:
    json.dump(tests_data, f, indent=2)
