from sys import platform as p
import os

if p == "linux" or p == "linux2":
    # linux
    os.system('pip3 install --upgrade tensorflow-gpu==1.14')
    os.system('pip3 install python-dotenv')
    os.system('pip3 install flask')
    os.system('pip3 install pillow')
    os.system('pip3 install requests')
    os.system('pip3 install numpy')
    print('\n\tAll requested packages are installed...')

elif p == "darwin":
    print('OS X')
    # OS X
    os.system('pip3 install --upgrade tensorflow-gpu==1.14')
    os.system('pip3 install python-dotenv')
    os.system('pip3 install flask')
    os.system('pip3 install pillow')
    os.system('pip3 install requests')
    os.system('pip3 install numpy')
    print('\n\tAll requested packages are installed...')

elif p == "win32":
    os.system('pip install --upgrade tensorflow-gpu==1.14')
    os.system('pip install python-dotenv')
    os.system('pip install flask')
    os.system('pip install pillow')
    os.system('pip install requests')
    os.system('pip install numpy')
    print('\n\tAll requested packages are installed...')
    # Windows...

else:
    print('\n\n\t\tWTF man!!')

exit()