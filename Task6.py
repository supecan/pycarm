ip_adr = input("Enter IP adress like 'x.x.x.x': ")
bin_octets = []

ip_correct=False
while not ip_correct:
    poit_count=ip_adr.count ( "." )
    if poit_count == 3:
        split_ip = ip_adr.split('.')
        for octets_ip in split_ip:
            if int ( octets_ip ) <= 255:
                if ip_adr == '0.0.0.0':
                    print ( 'unassigned' )
                    break
                elif ip_adr == '255.255.255.255':
                    print ( 'local broadcast' )
                    ip_correct=True
                    break
                elif int ( split_ip[ 0 ] ) < 223:
                    print ( 'unicast' )
                    ip_correct=True
                    break
                elif int ( split_ip[ 0 ] ) > 224 and int ( split_ip[ 0 ] ) < 239:
                    print ( 'multicast' )
                    ip_correct=True
                    break
                else:
                    print ( 'unused' )
                    ip_correct=True
                    break
            else:
                print ( "Number more: 255." )
                ip_adr = input("Enter IP again: ")


    else:
        print("Enter like: x.x.x.x")
        ip_adr = input("Enter IP again: ")
