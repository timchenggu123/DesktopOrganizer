# ----This is a simple tool for orgainizing my desktop space----
# Initializing the program...
import os
import glob
desk = 'C:\\Users\\TimGu\\Desktop'
typ = ['pdf', 'docx', 'mis','rtf']
content = os.listdir(desk)
# This creates a directory if it is not on desktop
for folder in typ:
    if not folder in content:
        os.makedirs(desk + '\\' + folder)

# This searches and move files
print(typ)
for filetyp in typ:
    i = 1
    files = glob.glob(desk + '\\*.' + filetyp)
    print (files)
    for file in files:
        print(os.listdir(desk + "\\" + filetyp))
        newname = file
        while os.path.basename(newname) in os.listdir(desk + "\\" + filetyp):
            oldname, ext = os.path.splitext(file)
            dgt = str(i)
            newname = oldname  + '(' +dgt+')' + ext
            i = i+1
        os.rename(file, desk + "\\" + filetyp + '\\' + os.path.basename(newname))
        print(desk + "\\" + filetyp + '\\' + os.path.basename(file))

# This section deal with miscellaneous files
folder = desk + "\\" + 'mis'
content = os.listdir(folder)
extbank = open(folder + "\\" + 'extbank.fc','a') # Creating the fc file if it doesn't already exit
extbank.write('')
extbank.close()
extbank = open(folder + "\\" + 'extbank.fc','r')
extlist = extbank.readlines()
extbank.close
extbank = open(folder + "\\" + 'extbank.fc','a')
extbank.write('')
templist = ['']
print(extlist)
for file in content:    # creating a list of extension tyes in a text file based on exsiting files in the folder
    ext = os.path.splitext(file)[1]
    if not ext + '\n' in extlist and not ext in templist:
        templist.append(ext)
        print(templist)
        extbank.write(ext + '\n')
extbank.close()

extbank = open(folder + "\\" + 'extbank.fc','r')
extlist = extbank.readlines()
extbank.close
content = os.listdir(desk)
print (extlist)
for file in content:
    file = desk + '\\' + file
    print(file)
    if os.path.splitext(file)[1] + '\n' in extlist and os.path.isfile(file):
        newname = file
        while os.path.basename(newname) in os.listdir(desk + "\\" + 'mis'):
            oldname, ext = os.path.splitext(file)
            dgt = str(i)
            newname = oldname  + '(' +dgt+')' + ext
            i = i+1
        os.rename(file, desk + '\\' + 'mis' + '\\'+ os.path.basename(newname) )
    
# Finishes the job...
wait = input('All done! Hit Enter to exit the program.')
