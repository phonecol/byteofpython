import os
import time

source = ['"D:\Lenovo\Desktop\Python\Python-Tutorial-Supplementary-Materials"']

target_dir = "D:\Lenovo\Desktop\Python\Python-Tutorial-Supplementary-Materials"

if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Enter a comment --> ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'
# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)



zip_command = 'zip -r  {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')