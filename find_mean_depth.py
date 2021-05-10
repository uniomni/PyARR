"""Test script that 

1. calculate the average or mean of the 10 numbers.
2. choose the file which is one up from the average (for example it
will be file '1%AEP10m_P6_unblocked_depth_max' and return the value
and filename.

Algorithm is very simplistic but will work well for small data sets

Ole Nielsen - 2021
"""

X = [('1%AEP10m_P4_unblocked_depth_max', 1.0737015),
     ('1%AEP10m_P8_unblocked_depth_max', 1.0736489),
     ('1%AEP10m_P7_unblocked_depth_max', 1.0767846),
     ('1%AEP10m_P6_unblocked_depth_max', 1.0747306),
     ('1%AEP10m_P2_unblocked_depth_max', 1.073645),
     ('1%AEP10m_P10_unblocked_depth_max', 1.0737189),
     ('1%AEP10m_P1_unblocked_depth_max', 1.0760777),
     ('1%AEP10m_P5_unblocked_depth_max', 1.0748001),
     ('1%AEP10m_P9_unblocked_depth_max', 1.0749958),
     ('1%AEP10m_P3_unblocked_depth_max', 1.0737971)]
     
# print(X)

# Sort by depth (Schwartzian Transform)
Y = [(d[1], d[0]) for d in X]  # Swap order, making depth the first column
Y.sort()

# Calculate average
sum = 0
for y in Y:
    sum += y[0]
    print('Element:', y)
avg = sum/len(Y)
print('Average is', avg)
print()

# Now find element immediately greater than average
i = 0
y = Y[0][0] 
while(y <= avg):
  i += 1
  y = Y[i][0]

depth = Y[i][0]
filename = Y[i][1]

print('Found filename:', Y[i][1])
print('Depth = ', Y[i][0])

    

