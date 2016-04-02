# can't have only 1 digit because not a sum
# max possible answer is less than 999999, because at that point 9^5 only adds 59049 
sum = 0
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                for m in range(0,10):
                    for n in range(0,10):
                        num = int(str(i) + str(j) + str(k) + str(l) + str(m) + str(n))
                        fifthpow =  pow(i,5) + pow(j,5) + pow(k,5) + pow(l,5) + pow(m,5) + pow(n,5)
                        if num == fifthpow:
                            print num
                            sum += num
                        
print sum - 1 
