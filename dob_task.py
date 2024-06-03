# Training

# opening folder
dob_content = ''

with open ('DOB.txt', 'r+') as file:
    for lines in file:
        dob_content += lines
    print('This is how the list of the .txt shows up:\n',dob_content)

# split the words as indexes
dob_content_list = dob_content.split()
print('This is everything split into multiple indexes:\n',dob_content_list, '\n')

# name the 2 lists
names_list = []
date_of_birth_list = []

# take only the names from the list and make them into a new list. index = 1 to 2.
# take only the dates of birth from list and make them into a new list. index = 3 to 5.
for i in range(0, len(dob_content_list), 5):    # Length to 5 as each person has 2 names (first and last) and 3 parts to their date of birth (D, M, Y).
    names_list.append(dob_content_list[i] + ' ' + dob_content_list[i+1] + '\n')
    date_of_birth_list.append(dob_content_list[i+2] + ' ' + dob_content_list[i+3] + ' ' + dob_content_list[i+4] + '\n')
    
print('Names only as indexes in list:\n ', names_list, '\n')
print('Date of Birth only as indexes in list:\n ', date_of_birth_list, '\n')

# Join names and dates of births back together as strings.
names_list_string  = ' '.join(names_list)
date_of_birth_list_string  = ' '.join(date_of_birth_list)

# Print the 2 lists separately.
print('Name:\n', names_list_string, '\n')
print('Date of Birth:\n', date_of_birth_list_string, '\n')

# python dob_task.py
# python and then type name of the file.
# Open in integrated terminal.


