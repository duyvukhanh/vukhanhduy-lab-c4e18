def is_inside(point,rec):
    if point[0] in range(rec[0],rec[0]+rec[2]+1) \
    and point[1] in range(rec[1],rec[1]+rec[3]+1):
        return True
    else: return False

#  Test case (ex 12):
# point_coor = [100 , 120]
# rec_coor = [140,60,100,200]
# is_inside = is_inside(point_coor,rec_coor)
# if is_inside:
#     print("Correct")
# else:
#     print("Wrong")



