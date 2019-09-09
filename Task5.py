from sys import argv

Ip_adress = argv[1]
IP_adress= Ip_adress.replace('/','.')
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