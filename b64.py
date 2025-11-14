#!/usr/bin/env python
import sys
import argparse
from base64 import \
  urlsafe_b64decode as b64decode, \
  urlsafe_b64encode as b64encode

__version__ = '0.2.0'

def b64dec(s:str) ->str:
    s += '=' * (-len(s) % 4)
    return b64decode(bytes(s, 'ascii')).hex()

def b64enc(s:str) ->str:
    return b64encode(bytes.fromhex(s)).rstrip(b'=').decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
      usage='b64.py [-h] [-e HEX] [-- vid]')
    parser.add_argument('vid', nargs='?', help='youtube video id into hex')
    parser.add_argument('-e', dest='hex', help='hex into youtube video id')
    args = parser.parse_args()
    if args.vid:
      print(b64dec(args.vid))
    elif args.hex:
      print(b64enc(args.hex))
    else:
      parser.print_help()
