import argparse
import socket
from sys import stdout

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('-o', dest='output', type=str, required=False, default=None)
cmdlineArgs = vars(parser.parse_args())

outFile = open(cmdlineArgs['output'], 'w+') if cmdlineArgs['output'] else None

try:
    with open(cmdlineArgs['input'], 'r') as inFile:
        for line in inFile:
            host = line.strip()
            try:
                ip = socket.gethostbyname(host)
            except socket.gaierror:
                ip = 'none'
            outLine = '%s,%s\n' % (host, ip)
            stdout.write(outLine)

            if outFile:
                outFile.write(outLine)
finally:
    if outFile:
        outFile.close()
