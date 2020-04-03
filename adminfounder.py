# Import Moduls
try:
    import os
except ImportError:
    print ("\033[31m[-] You Don't Have os Module")
try:
    import requests
except ImportError:
    print ("\033[31m[-] You Don't Have requests Module")
try:
    import sys
except ImportError:
    print ("\033[31m[-] You Don't Have sys Module")
# Banner Function
def banner():
    print ('#'*49)
    print ('# Create By Mr Submissive in 2018               '  + '#')
    print ('# Token Brute Force Script For Python 3.X.X' + '\t' + '#')
    print ('# Github : https://github.com/MrSubmissive' +'\t'*1+ '#')
    print ('# Thank You For Support us' +'\t'*3+ '#')
    print ('#'*49)
    print ("\n\033[32mUsage: python3 adminfounder.py -u URL")



# Main Function
def exploit(url):
    try:
        request = requests.get(url)
        if request.status_code == 200:
            print ("\033[32m[+] I Found This: " + url)
        else:
            print ("\033[31m[-] I Can't Found This: " + url)
    except Exception as e:
        print ("\033[31m[-] Connection Error !")
def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == "-u" or sys.argv[1] == "-U":
            if "https://" in sys.argv[2]:
                url = sys.argv[2]
            elif "http://" in sys.argv[2]:
                url = sys.argv[2]
            else:
                url = "http://" + sys.argv[2]
            if not os.path.exists("Founder.txt"):
                print ("\033[31m[-] My File Is Lost Please Install This Script Again")
                sys.exit()
            else:
                read = open("Founder.txt")
                for lines in read.read().splitlines():
                    line = lines.strip()
                    if line == "":
                        continue
                    if line.find(".") == -1:
                        line = line + "/"
                        url1 = url + "/" +line
                        exploit(url1)
        elif sys.argv[1] != "-h" or sys.argv[1] != "-H":
            print ("\033[31m[-] You Command Is Not True !")
    if len(sys.argv) == 2 and sys.argv[1] == "-h" or sys.argv[1] == "-H":
        banner()
    if len(sys.argv) > 3:
        banner()
try:
    main()
except Exception:
    print ("\033[31m[-] Some Thing Wrong !\nWe exit soon...!")
    exit()
