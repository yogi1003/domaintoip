from socket import gethostbyname as gh, gaierror
import tldextract
import argparse

parser = argparse.ArgumentParser(description="CHANGE DOMAIN TO IP")
parser.add_argument("infile", type=str, help="List Name")
parser.add_argument("outfile", type=str, help="Output Name")
args = parser.parse_args()

resip = set()
weblist = open(args.infile).read().splitlines()

with open(args.outfile, "a+") as result:
    for x in weblist:
        i = gh(tldextract.extract(x).registered_domain)
        if i not in resip:
            resip.add(i)
            result.write(i+"\n")
            print(i)
