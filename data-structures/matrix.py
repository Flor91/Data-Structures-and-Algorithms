from numpy import * 

"""
 Recording temprature for 1 week measured in the morning, mid-day, evening and mid-night. 
 It can be presented as a 7X5 matrix using an array and the reshape method available in numpy.
"""
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = reshape(a,(7,5))
print(m)

"""
Prints:
[['Mon' '18' '20' '22' '17']
 ['Tue' '11' '18' '21' '18']
 ['Wed' '15' '21' '20' '19']
 ['Thu' '11' '20' '22' '21']
 ['Fri' '18' '17' '23' '22']
 ['Sat' '12' '22' '20' '18']
 ['Sun' '13' '15' '19' '16']]
"""

# Print data for Wednesday
print(m[2])

# Print data for friday evening
print(m[4][3])

# Adding a row
m_r = append(m,[['Avg',12,15,13,11]],0)

# Adding a column
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)

# Delete a row
m = delete(m,[2],0)

# Delete a column
m = delete(m,s_[2],1)

# Update a row
m[3] = ['Thu',0,0,0,0]