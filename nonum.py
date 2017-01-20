import os,re
for file in os.listdir("C:\\users\\desktop"):
    if not(re.search(r'\d', file)):
        print(file)        