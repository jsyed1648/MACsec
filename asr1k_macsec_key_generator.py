import random
import string
import datetime

start_date = datetime.datetime.now()

def key_generator (size=64, chars=string.hexdigits + string.digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

for key in range (1,64):
    print "key %.2d" % key
    print "cryptographic-algorithm aes-256-cmac"
    print "key-string {}".format(key_generator())
    key_start_date = (start_date + datetime.timedelta(days=9*(key-1))).strftime("%T %b %d %Y")
    print "lifetime {} duration 864000".format(key_start_date)

print "key 64\ncryptographic-algorithm aes-256-cmac"
print "key-string {}".format(key_generator())