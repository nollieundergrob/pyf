import subprocess
import os
def proccescheck(cd):
    # print(cd)
    f = filter(str.isalpha, cd)
    namefile = "".join(f)
    # print(namefile)
    with open('assets\\storage\\dir_info_'+str(namefile)+'.txt', 'w') as txt:
        txt.write(subprocess.check_output('tree '+cd+' /f /a', shell=True).decode('cp866'))
      