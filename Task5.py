from sys import argv
'''name_r = input("Enter name Router: ")
name_param = input("Inter name parametr(ios, model, vendor, location, ip)".lower())
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
print(london_co[name_r])
print(london_co[name_r][name_param])'''


IP_adress= input("Enter IP adres").replace('/','.')
IP_adress = IP_adress.split(".")
int(IP_adress[0])
int(IP_adress[1])
int(IP_adress[2])
int(IP_adress[3])
mask = IP_adress.pop(-1)
mask = int(mask)
msk = (mask * '1') + ((32 - mask) * "0")
print(msk)


ip_template = '''
    ...: IP address:
    ...: {:<08b} {:<08b} {:<08b} {:<08b}
    ...: '''

mask_template = '''
    ...: Mask:
    ...: {} {} {} {}
    ...: '''


print(ip_template.format(int(IP_adress[0]), int(IP_adress[1]),int(IP_adress[2]), int(IP_adress[3])))
print(mask_template.format(msk[0:8], msk[8:16], msk[16:24], msk[24:32]))