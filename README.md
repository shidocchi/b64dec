# b64dec
decode youtube video id into hexadecimal

## Usage

    $ python -m b64dec AAAAAAAAAAA
    0000000000000000

    $ python -m b64dec __________8
    ffffffffffffffff

## Notice

Because urlsafe-base64 string includes '-' (minus sign)

    $ python -m b64dec -h
    fa

    $ python -m b64dec --help
    fbe85e96

use '+' (plus sign) for prefix character

    $ python -m b64dec +h
    usage: b64dec.py [+h] vid

    positional arguments:
      vid         youtube video id

    optional arguments:
      +h, ++help  show this help message and exit
