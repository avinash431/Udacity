from functools import wraps
import time

def timer(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print (
            "@timer:" + fn.func_name + " took " + str(t2 - t1) + " seconds")
        return result
    return measure_time
