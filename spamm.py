import os, time, requests
G0 = '\x1b[0;32m'
G1 = '\x1b[1;32m'
C0 = '\x1b[0;36m'
C1 = '\x1b[1;36m'
P0 = '\x1b[0;35m'
P1 = '\x1b[1;35m'
W0 = '\x1b[0;37m'
W1 = '\x1b[1;37m'
B0 = '\x1b[0;34m'
B1 = '\x1b[1;34m'
R0 = '\x1b[0;31m'
R1 = '\x1b[1;31m'
BG = '\x1b[1;97;41m'
RE = '\x1b[0m'
dark = print

def balik():
    dark('%s[%sx%s] %sExiting Program' % (W0, R1, W0, R0))
    dark('%s[%sx%s] %sKunjungi web kami http://www.22xploitercrew.tech' % (W0, R1, W0, R0))
    os.system('xdg-open http://www.youtube.com/c/ParkerzGans')
    exit(1)


def logo():
    os.system('clear')
    dark('\n\n%s   _  _     \n%s _| || |_    %sTools SpamCall%s\n%s|_  ..  _|  %s[%s22XploiterCrew%s]\n%s|_      _|     %s[%sC4L4MITY%s]\n%s  |_||_|\n%s----------------------------' % (C1, C1, BG, RE, C1, R0, W0, R0, C1, R0, W0, R0, C1, P0))


def menu():
    dark('%s[%s1%s] %sSpam Grab\n%s[%s2%s] %sSpam Oyo\n%s[%s3%s] %sSpam Telkom\n%s[%s0%s] %sExit\n' % (W0, C1, W0, C0, W0, C1, W0, C0, W0, C1, W0, C0, W0, R1, W0, C0))


shas = input

def inp():
    try:
        das = ['1', '2', '3', '0']
        pilih = shas('%s╔%s[%s22XC%s]\n%s╚%s[%sPilih%s]> %s' % (P1, R1, W1, R1, P1, R1, W1, R1, C1))
        while 1:
            if pilih not in das:
                logo()
                menu()
                dark('\n%s[%sx%s] %sPilihan Anda salah' % (W0, R1, W0, R0))
                pilih = shas('%s╔%s[%s22XC%s]\n%s╚%s[%sPilih%s]> %s' % (P1, R1, W1, R1, P1, R1, W1, R1, C1))

        if pilih == '1':
            os.system('cd sc; python2 grab.py')
        else:
            if pilih == '2':
                os.system('cd sc; python2 oyo.py')
            else:
                if pilih == '3':
                    os.system('cd sc; python2 telkom.py')
                else:
                    if pilih == '0':
                        balik()
    except KeyboardInterrupt:
        balik()


if __name__ == '__main__':
    logo()
    menu()
    inp()
