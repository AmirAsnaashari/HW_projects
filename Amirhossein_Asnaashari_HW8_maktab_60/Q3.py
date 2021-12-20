import re

pm = re.compile(r'.*\b(world)$')
has = pm.match("He is the greatest Athlete in the world")
print(has)
