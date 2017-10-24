# coding: utf-8

from common import add

rslt = add.delay(1, 3)

# 38121448-1d17-4b1e-a6ff-0d37bf9664e9
print '[add]id = ', rslt.id
