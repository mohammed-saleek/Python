from datetime import datetime
from datetime import timedelta
import random
import uuid
import math

x = datetime.now() + timedelta(days=10)
print(x)
print(x.strftime('%A'))

x = random.randint(1234,9876)
print(x)

a = uuid.uuid4()
print(a)

b = math.factorial(3)
x = math.ceil(5.3)
y = math.fabs(5/2)
print(b)
print(x)
print(y)

import os

if os.path.exists("py.txt"):
    os.remove("py.txt")
