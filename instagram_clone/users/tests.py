# from django.test import TestCase


from string import digits
from random import choices
# l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
a = "".join(choices(digits, k=4))

print(a)
