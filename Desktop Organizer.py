# ----This is a simple tool for orgainizing my desktop space----
# Initializing the program...
import os
import glob

# Creating Constant variables
desk = 'C:\\Users\\TimGu\\Desktop'
typ = ['pdf', 'docx', 'mis','rtf']                                               # You can customize this list to include different file extension'
content = os.listdir(desk)

# Defining neccessary functions
def createfc(folder):
    extbank = open(folder + "\\" + 'extbank.fc','a')                                # Creating the fc file if it doesn't already exit
    extbank.write('')                                                               # Appending an empty string to create the file
    extbank.close()

def updatefc(folder):
    content = os.listdir(folder)
    extbank = open(folder + "\\" + 'extbank.fc','r')                                #reading the existing folder list
    extlist = extbank.readlines()
    extbank.close

    extbank = open(folder + "\\" + 'extbank.fc','a')
    extbank.write('')

    templist = ['']
    print(extlist)
    for file in content:                                                            # creating a list of extension tyes in a text file based on exsiting files in the folder
        ext = os.path.splitext(file)[1]
        if not ext + '\n' in extlist and not ext in templist:
            templist.append(ext)
            print(templist)
            extbank.write(ext + '\n')
    extbank.close()

def grabfiles(folder):
    i = 1
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
            while os.path.basename(newname) in os.listdir(desk + "\\" + foldername):
                oldname, ext = os.path.splitext(file)
                dgt = str(i)
                newname = oldname  + '(' +dgt+')' + ext
                i = i+1
            os.rename(file, desk + '\\' + foldername + '\\'+ os.path.basename(newname) )
            

# creating new folders
while True:
    foldername = input("Please enter the name of the smart folder to create a new one. To skip or proceed, hit enter")
    print(bool(foldername))
    if not bool(foldername):
        break
    foldername = foldername + '[!smart!]'
    if not foldername in content:
        folder = desk + "\\" + foldername
        os.makedirs(folder)
        createfc(folder)
        content = os.listdir(desk)                                              # Update the list of directories
        print(desk + '\\' + foldername + ' has been successfully created')
    else:
        print('The folder name already exist. Please enter a new one')

# grabbing files
content = os.listdir(desk)                                                      # Update the list of directories
print(content)
for path in content:
    if path.find('[!smart!]') > 0:
        print(path.find('[!smart!]!'))
        print(path)
        folder = folder = desk + "\\" + path
        createfc(folder)
        updatefc(folder)
        grabfiles(folder)



### This creates a directory if it is not on desktop
##for folder in typ:
##    if not folder in content:
##        os.makedirs(desk + '\\' + folder)
##
### This searches and move files
##print(typ)
##for filetyp in typ:
##    i = 1
##    files = glob.glob(desk + '\\*.' + filetyp)
##    print (files)
##    for file in files:
##        print(os.listdir(desk + "\\" + filetyp))
##        newname = file
##        while os.path.basename(newname) in os.listdir(desk + "\\" + filetyp):
##            oldname, ext = os.path.splitext(file)
##            dgt = str(i)
##            newname = oldname  + '(' +dgt+')' + ext
##            i = i+1
##        os.rename(file, desk + "\\" + filetyp + '\\' + os.path.basename(newname))
##        print(desk + "\\" + filetyp + '\\' + os.path.basename(file))
##
### This section deal with miscellaneous files
##folder = desk + "\\" + 'mis'
##content = os.listdir(folder)
##
##extbank = open(folder + "\\" + 'extbank.fc','a')                                # Creating the fc file if it doesn't already exit
##extbank.write('')                                                               # Appending an empty string to create the file
##extbank.close()
##
##extbank = open(folder + "\\" + 'extbank.fc','r')                                #reading the existing folder list
##extlist = extbank.readlines()
##extbank.close
##
##extbank = open(folder + "\\" + 'extbank.fc','a')
##extbank.write('')
##
##templist = ['']
##print(extlist)
##for file in content:                                                            # creating a list of extension tyes in a text file based on exsiting files in the folder
##    ext = os.path.splitext(file)[1]
##    if not ext + '\n' in extlist and not ext in templist:
##        templist.append(ext)
##        print(templist)
##        extbank.write(ext + '\n')
##extbank.close()
##
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

### Finishes the job...
##wait = input('All done! Hit Enter to exit the program.')
