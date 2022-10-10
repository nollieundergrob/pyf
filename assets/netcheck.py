import socket
import subprocess
def proccescheck():
    arp =  subprocess.check_output('arp -a', shell = True )
    routetable = subprocess.check_output('route print', shell = True)
    ip = socket.gethostbyname_ex(socket.gethostname())
    with open('assets\\network\\net_info.cfg', 'w') as txt:
        txt.write(str(ip)+"\n\n===========================================================================\n\n"+arp.decode('cp866')+"\n\n"+routetable.decode('cp866'))