from asyncio import subprocess
import socket
import subprocess
import getpass
from assets import netcheck
from assets import dircheck

def main():
    answer = input('Выбор действия:\n1)Информация о подсети \n2)Информация о директориях\n3)Работа с директориями\n\n')
    if answer == "1":
        netcheck.proccescheck()
    elif answer == "2":
        cd = input('Введите директорию (нап-р: С:\\Users\\'+getpass.getuser()+')\n\n')
        dircheck.proccescheck(cd)
    elif answer == "3":
        pass
    else:
        print("Не понимаю")
        main()


if __name__ == "__main__":
    main()

