import win32com.client
from docutils.utils.math.math2html import file


def get_file_metadata(path, filename):
    metadata = ['Name', 'Size', 'Item type', 'Date modified', 'Date created']
    # Path shouldn't end with backslash, i.e. "E:\Images\Paris"
    # filename must include extension, i.e. "PID manual.pdf"
    # Returns dictionary containing all file metadata.
    sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)
    ns = sh.NameSpace(path)

    # Enumeration is necessary because ns.GetDetailsOf only accepts an integer as 2nd argument
    file_metadata = dict()
    item = ns.ParseName(str(filename)) #In SQL Server, you can use the PARSENAME() function to return part of an object name.

    for ind, attribute in enumerate(metadata):
        attr_value = ns.GetDetailsOf(item, ind)
        if attr_value:
            file_metadata[attribute] = attr_value

    print("metaData is : " )
    print(file_metadata)

    return file_metadata

# *Note: you must know the total path to the file.*
# Example usage:
#if __name__ == '__main__':
'''
folder = 'E:\\computers\\level 4\\semester 1\\selected 3\\project\\arabiya\\Test\\Finance'
filename = '#كيف_تجني_المال؟-معمل-لصناعة-ساعات-الحائط.txt'

print(get_file_metadata(folder, filename))

'''


#########################################################################

# !usr/bin/env python
# This program displays metadata from pdf file
"""
from win32com.client import Dispatch
shell = Dispatch("Shell.Application")
_dict = {}
# enter directory where your file is located
ns = shell.NameSpace("E:\computers\level 4\semester 1\selected 3\project")
for i in ns.Items():
    # Check here with the specific filename
    if str(i) == "Selected 3 -  project Ideas.pdf":
        for j in range(0,150):
            _dict[ns.GetDetailsOf(j,j)] = ns.GetDetailsOf(i,j)

print (_dict)


"""


