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
    parser = argparse.ArgumentParser(prefix_chars='+')
    parser.add_argument('vid', help='youtube video id')
    args = parser.parse_args()
    print(b64dec(args.vid))
