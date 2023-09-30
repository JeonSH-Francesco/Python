from sys import getsizeof
import time

#list comprehension
comprehension = [num**2 for num in range(100000)]
startTime = time.time()
sum_comprehension = sum(comprehension)
print("comprehension time: %f" % (time.time() - startTime))
print("comprehension memory size: %d bytes, which means %.2f MB." % (getsizeof(comprehension), getsizeof(comprehension) / 1024 / 1024))

#generator
generator=(num**2 for num in range(100000))
startTime=time.time()
sum_generator=sum(generator)
print("generator time : %f"%(time.time()-startTime))
print("generator memory size: %d"%getsizeof(generator))
