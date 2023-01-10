import os
import re

path = "E:\\computers\\level 4\\semester 1\\selected 3\\project\\arabiya\\Test\\Finance"

# Change the directory
os.chdir(path)

import os
import re

pattern = r""
array1 = []
def extractTitleAndPublisher (file) :
    with open(file, "r", encoding='utf-8') as data:
        #print(data.read())
        #array1 = array1 + re.findall(pattern, data.read(), re.MULTILINE)
        #s = 'Part 1. Part 2. Part 3 then more text'
        #print(re.search(r'Part 1\.(.*?)\. Part 3', s).group(1))
        fileData = data.read()
        title = re.search(r'Title\n(.*?)\nSource', fileData).group(1)
        print("title is : " + title)
        print( "publisher is : " +re.search(r'Source\n(.*?)\nBody', fileData ).group(1) )
        print( "body is : " +re.search(r'Body\n(.*?)\n', fileData ).group(1) )
        print()
        return  re.search(r'Body\n(.*?)\n', fileData ).group(1)
'''
for file in os.listdir():
    extractTitleAndPublisher(file)
'''

