# Exercise 54 - Modifying Multilevel Dictionaries
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

d['employees'][1]['lastName'] = 'SillyWalks'
print(d['employees'][1]['lastName'])