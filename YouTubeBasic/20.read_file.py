
"""
r = read file
w = write file
a = append at the end file
r + = read and write
"""

emp_file = open('README.md', 'r')
# print(emp_file.readable()) # returns file is readable or not => TRUE or FALSE
# print(emp_file.readline()) # returns a single of a file
# print(emp_file.read()) # returns all lines
# print(emp_file.readlines())  # put into an array
for emp in emp_file.readlines():
    print(emp)
emp_file.close()
