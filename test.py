a = [5, 1, 3, 4, 7]
a.sort()
x = 12
count = 0
print(a)
li = []
for i in range(len(a)-2):
    left = i+1
    right = len(a)-1
    while right > left:
        if a[left] + a[right] +a[i] < x:
            count += right-left

            left += 1
        else:
            right-=1
print(count)





    


        


    






    

