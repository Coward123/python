
import random, string
field = string.letters + string.digits
def getRandom():
    return ''.join(random.sample(field,4))
def getString(m):
    return '-'.join([getRandom() for i in range(m)])
def generate(n):
    return [getString(4) for i in range(n)]
print generate(20)

import uuid
print uuid.uuid1()
print uuid.uuid4()
