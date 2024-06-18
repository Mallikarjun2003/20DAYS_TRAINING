# ip : [2,5,2,3,6,7,1,0,5] op :14
# ip:[2,5,2,3,6,7,1,0,5,7] op :20
buildings = [2,5,2,3,6,7,1,0,5,7]
n = len(buildings)
left_max_building = [0]*n
right_max_building = [0]*n
left_max_building[0] = buildings[0]
right_max_building[n-1] = buildings[n-1]

for i in range(1,n):
    left_max_building[i] = max(left_max_building[i-1], buildings[i])
for i in range(n-2,-1,-1):
    right_max_building[i] = max(right_max_building[i+1], buildings[i])
water = 0
for i in range(n):
    water += min(left_max_building[i], right_max_building[i]) -buildings[i]
print(water)



