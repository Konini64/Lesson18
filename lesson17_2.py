import re

line = "The ghost that says boo haunts the loo."

m = re.findall("oo", line , re.IGNORECASE)

print(m)

match = re.findall(".oo", "The ghost that says tBoo haunts the loo.")
print(match)