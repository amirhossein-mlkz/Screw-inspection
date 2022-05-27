

import time

time1=time.time()

for i in range(10000):

    

    eval(str(i*25))


time2=time.time()

for i in range(10000):

    

    str(i*25)

time3=time.time()


print('eval',time2-time1)

print('not eval',time3-time2)