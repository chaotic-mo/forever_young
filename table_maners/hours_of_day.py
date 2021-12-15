#De eerste is in twee for in's gesliptst om de AM en PM te verduidelijke
'''
for i in range(1, 13):
     print(str(i),' am')
for i in range(13, 25):
     print(str(i),' pm')
'''
#De tweede is met een if else stament om het korter te proberen te schrijven
for i in range(1, 25):
    if i < 13:
        print(i, ' am')
    else:
        print(i, ' pm')


