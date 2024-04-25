def equal_stack(h1, h2, h3):
    ptr1, ptr2, ptr3 = 0, 0, 0
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)

    while True:
        if ptr1 == len(h1) or ptr2 == len(h2) or ptr3 == len(h3):
            return 0
        if sum1 == sum2 == sum3:
            return sum1
        max_height = max(sum1, sum2, sum3)
        if sum1 == max_height:
            sum1 -= h1[ptr1]
            ptr1 += 1
        elif sum2 == max_height:
            sum2 -= h2[ptr2]
            ptr2 += 1
        elif sum3 == max_height:
            sum3 -= h3[ptr3]
            ptr3 += 1


h1 = [3, 2, 1, 1, 1]  
h2 = [4, 3, 2]       
h3 = [1, 1, 4, 1]     

print(equal_stack(h1,h2,h3))
