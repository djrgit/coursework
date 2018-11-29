# Exercise 58 - Add to JSON
import json
from pprint import pprint

with open('company1.json', 'r+') as f:
	d = json.loads(f.read())
	d['employees'].append(dict(firstName= 'Albert', lastName= 'Bert'))
	f.seek(0)
	json.dump(d, f, indent=4, sort_keys=True)
	f.truncate()