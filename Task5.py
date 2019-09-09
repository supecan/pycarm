mode = input("Enter mode: (access/trunk )")
interface = input("Enter number interface ")
vlan = input("Enter VLAN")



access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]



template = {'access':access_template, 'trunk':trunk_template}

print('interface {}'.format(interface))
print('\n'.join(template[mode]).format(vlan))





'''
trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

print('interface {}'.format(interface))

vlan = input('Enter VLAN number: ')

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
print('\n'.join(access_template).format(vlan))
'''