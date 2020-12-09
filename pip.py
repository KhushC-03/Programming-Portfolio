# Pip Installer #Khush Chauhan
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:86.1) Gecko/20100101 Firefox/86.1'
}
import os, requests, time
from bs4 import BeautifulSoup

v = requests.session()
url = 'https://pypi.org/project/'
main_string  = 'pip install'
def install(prefix,url):
    I1 = input('Enter the name(s) of the packages you would like to install, seperate them with a comma: ')
    if ',' in I1:
        packages = I1.split(',')
        for package in packages:
            r = v.get(f'{url}{package}', headers=headers)
            soup = BeautifulSoup(r.content,'html.parser')
            try:
                packagename = soup.find_all('span')[6]
                name = f'{prefix} {package}'
                if str(packagename.text) == str(name):
                    print(f'Installing {package}')               
                    os.system(name)
                else:
                    print('Package Does Not Exist!')
                    pass        
            except:
                print('Package Does Not Exist!')
                pass
        

    else:
        r = v.get(f'{url}{I1}', headers=headers)
        soup = BeautifulSoup(r.content,'html.parser')
        try:
            packagename = soup.find_all('span')[6]
            package = packagename
            name = f'{prefix} {I1}'
            if str(package.text) == str(name):
                print(f'Installing {I1}') 
                I = os.system(str(name))
                print('Package is installed!')
            else:
                print('Package Does Not Exist!')
      
        except:
            print('Package Does Not Exist!')
 

def pip_update():
    try:
        os.system('pip install --upgrade pip')
        time.sleep(1)

    except Exception as ex:
        print('Could Not Update')
  
def see_packages():
    try:
        os.system('pip list')

    except Exception as ex:
        print('Could Not list Packages')

def delete_packages():
    prefix = 'pip uninstall'
    I1 = input('Which package(s) would you like to uninstall? Seperate them with a comma: ')
    if ',' in I1:
        packages = I1.split(',')
        for package in packages:
            try:
                print(f'Uninstalling {package}') 
                os.system(f'{prefix} {package}')
                print('Package installed')  
            except:
                print('Package could not be uninstalled!')
    else:
        try:
            print(f'Uninstalling {I1}') 
            I = os.system(f'{prefix} {I1}') 
            print('Package installed')     
        except:
            print('Package could not be uninstalled!')


def menu():
    os.system('cls')
    print('\n\x1b[1;37mWelcome to the Pip Package Installer for Python! ')
    print('[1] : Install Pip Packages')
    print('[2] : Update Pip')
    print('[3] : See Installed Packages')
    print('[4] : Delete Packages')
    print('[5] : Exit')
    I1 = int(input(' '))
    if I1 == 1:
        install(main_string, url)
        input('Click enter to finish!')
        menu()
    elif I1 == 2:
        pip_update()
        input('Click enter to finish!')
        menu()
    elif I1 == 3:
        see_packages()
        input('Click enter to finish!')
        menu()
    elif I1 == 4:
        delete_packages()
        input('Click enter to finish!')
        menu()
    elif I1 == 5:
        os.system('cls')
        os.system('exit')
    else:
        print('\x1b[1;31mInvalid Selection')
        time.sleep(1)
        os.system('cls')
        menu()
menu()
