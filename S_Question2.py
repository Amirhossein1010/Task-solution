def getMedian(num1 , num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    
    x= len(num1)
    y = len(num2)

    low =0 
    high = x
    while low <= high:
        px = (low + high) // 2
        py = ((x + y + 1) // 2) - px

        maxLeftNum1 = num1[px - 1] if px > 0 else float("-infinity")
        minRightNum1 = num1[px] if px != x else float("infinity")

        maxLeftNum2 = num2[py - 1] if py > 0 else float("-infinity")
        minRightNum2 = num2[py] if py != y else float("infinity")    

        if (maxLeftNum1 <= minRightNum2) and (maxLeftNum2 <= minRightNum1):
            if (x + y) % 2 == 0:  
                return (max(maxLeftNum2, maxLeftNum1) + min(minRightNum1, minRightNum2)) / 2
            else:    
                return max(maxLeftNum1, maxLeftNum2)

        elif maxLeftNum1 > minRightNum2:
            high = px - 1
        else:
            low = px + 1


num1 = list(map(int, input()[1:-1].split(',')))
num2 = list(map(int, input()[1:-1].split(',')))
answer = getMedian(num1, num2)
print("%.5f" % answer)   