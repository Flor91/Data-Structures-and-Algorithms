import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

""" 
We create two dictionaries and club them using the ChainMap method from the collections library. 
Then we print the keys and values of the result of the combination of the dictionaries. 
If there are duplicate keys, then only the value from the first key is preserved.
"""
res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps,'\n')
# [{'day1': 'Mon', 'day2': 'Tue'}, {'day1': 'Thu', 'day3': 'Wed'}] 

print('Keys = {}'.format(list(res.keys())))
# Keys = ['day1', 'day3', 'day2']
print('Values = {}'.format(list(res.values())))
# Values = ['Mon', 'Wed', 'Tue']


# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
# day1 = Mon
# day3 = Wed
# day2 = Tue

# Find a specific value in the result
print('day3 in res: {}'.format(('day1' in res))) 
# day3 in res: True

# Updating a value in one of the original dictionaries, will automatically update the value in the ChainMap
dict2['day4'] = 'Fri'

print(res.maps,'\n')
# [{'day1': 'Mon', 'day2': 'Tue'}, {'day1': 'Thu', 'day3': 'Wed', `day4`: `Fri`}] 