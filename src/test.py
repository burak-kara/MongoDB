from datetime import datetime
import time

ts1 = datetime.timestamp(datetime.now())
time.sleep(2)
ts2 = datetime.timestamp(datetime.now())
result = ts2 - ts1

ts1 = time.time()
time.sleep(2)
ts2 = time.time()
result2 = ts2 - ts1

print("{} seconds".format(round(result, 3)))
print("{} seconds".format(round(result2, 3)))
