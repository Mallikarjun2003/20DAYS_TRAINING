# determine on which buildings the sunlight falls morning and evenings left and right
# [3,5,9,6,8,10] op :Morning =  4 evening =  1
buildings = [3,4,5,10,4,3]
cur_max = 0
will_fall_in_mrng = 0
for i in range(len(buildings)):
    if buildings[i] > cur_max:
        cur_max = buildings[i]
        will_fall_in_mrng+=1
cur_max = 0
will_fall_in_eve = 0
for i in buildings[::-1]:
    if i > cur_max:
        cur_max = i
        will_fall_in_eve+=1
print("Morning = ",will_fall_in_mrng,"evening = ",will_fall_in_eve)
