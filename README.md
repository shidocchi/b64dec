# b64dec
decode youtube video id into hexadecimal

- YouTubeなどで使われる「BASE64文字列 (URL-safe)」を「16進数文字列」に置き換えます
- yt-dlpなどで録画を行う際、ファイル名生成に使用しています

## Usage

You can convert 11-digit base64 string into 8-byte hexadecimal string:

    $ python -m b64 -- AAAAAAAAAAA
    0000000000000000

    $ python -m b64 -- __________8
    ffffffffffffffff

You can use '-' (minus sign) as optional argument either urlsafe-base64 string contains the character:

    $ python -m b64 -- -----------
    fbefbefbefbefbef

    $ python -m b64 --help
    usage: b64.py [-h] [-e HEX] [-- vid]

    positional arguments:
      vid         youtube video id into hex

    options:
      -h, --help  show this help message and exit
      -e HEX      hex into youtube video id

You can also convert hexadecimal string into base64 string:

    $ python -m b64 -e 0000000000000000
    AAAAAAAAAAA
