# Addy Gen
import os,requests, time
def addygen():
    os.system('cls')
    address_file = os.path.exists('STORES\\Tools\\addesses.txt')
    if address_file == False:
        a = open('STORES\\Tools\\addesses.txt','w')
        addygen()
    elif address_file == True:
        amount = int(input('\x1b[1;37mHow Many Addresses Would You Link To Generate\x1b[1;36m?\x1b[1;37m '))
        print("""                AL B BA BB BD BH BL BN BR BS CA CB CF CH CM CO CR CT CV CW D
                A DE DH DL DN DT DY E EC EN EX FY GL GU HA HD HG HP HR HU HX
                IG IP KT L LA LD LE LL LN LS LU M ME MK N NE NG NN NP NR NW OL 
                OX PE PL PO PR RG RH RM S SA SE SG SK SL SM SN SO SP SR SS ST 
                SW SY TA TF TN TQ TR TS TW UB W WA WC WD WF WN WR WS WV YO""")
        postcode = input('\x1b[1;37mPost Code Prefix \x1b[1;36m:\x1b[1;37m ')
        headers = {
            'authority': 'www.doogal.co.uk',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51',
            'x-requested-with': 'XMLHttpRequest',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.doogal.co.uk/RandomAddresses.php',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
            'cookie': '_ga=GA1.3.926399585.1600422616; _gid=GA1.3.619049017.1600422616; _gat=1',
        }

        params = {
            'startWith', postcode
            }
        
        for i in range(amount):
            r = requests.get('https://www.doogal.co.uk/CreateRandomAddress.ashx', headers=headers, params=params)
            address = r.text
            if len(address.split(','))==3:
                addy = address.split(',')
                mainaddress = ('{} {} {} \n').format(addy[0],addy[1],addy[2])
                mainaddress1 = ('{} {} {}').format(addy[0],addy[1],addy[2])
                addys = open('STORES\\Tools\\addesses.txt','a')
                addys.write(str(mainaddress))
                print(mainaddress1)
            elif len(address.split(','))==4:
                addy = address.split(',')
                mainaddress = ('{} {} {} \n').format(addy[0],addy[1],addy[2])
                mainaddress1 = ('{} {} {}').format(addy[0],addy[1],addy[2])
                addys = open('STORES\\Tools\\addesses.txt','a')
                addys.write(str(mainaddress))
                print(mainaddress1)
            elif len(address.split(','))==5:
                addy = address.split(',')
                mainaddress = ('{} {} {} \n').format(addy[0],addy[1],addy[2],addy[3])
                mainaddress1 = ('{} {} {}').format(addy[0],addy[1],addy[2],addy[3])
                addys = open('STORES\\Tools\\addesses.txt','a')
                addys.write(str(mainaddress))
                print(mainaddress1)
        addys.close()  