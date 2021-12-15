# Subarray with 0 sum

# Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

array = [ 4 , 2 , -3 , 1 , 6 ]
ans = []

for interval_length in range ( 1 , len ( array ) ) :
    
    for index in range ( 0 , len ( array ) - interval_length ) :
        
        temp = array [ index : index + interval_length + 1 ]
        if sum ( temp ) == 0 : ans .append ( temp )

print ( ans )