import re
text  = "this is a good day"

if re.search("good",text):
    print(":)")
else:
    print(":(")
    

text = "Amy works diligently. Amy gets good grades.Our Amy is successful"

if re.search("^Amy",text):
    print("heue")

grades = "AcAAAABCBCBAA"

p = re.findall("B",grades)

