import sys
import os.path
import binascii
import string

def check_file_provided():
    # 指定した先にファイルが存在するかをチェック
    default_path = "./rakupan.png"

    if (len(sys.argv) < 2):
        print("")
        print("Warning")
        print("Correct Usage : python read_bin.py <file_name>")
        print("")
        print("call {0}".format(default_path))
        if not os.path.isfile(default_path):
            print("")
            print("Error - The file provided does not exist")
            print("")
            sys.exit(0)
        else:
            print("{} is exist".format(default_path))
            print("")

            return default_path
    else:
        print("")
        print("{} is exist".format(sys.argv))
        print("")

        return sys.argv[1]

def read_bytes(filename, chunksize=8192):
    # バイナリファイルをバイトごとに抽出
    try:
        with open(filename, "r+b") as f:
            while True:
                chunk = f.read(chunksize)
                if chunk:
                    for b in chunk:
                        #print(type(b))
                        #print(b)
                        yield b
                else:
                    break
    except IOError:
        print("")
        print("Error - The file provided can't open")
        print("")
        sys.exit(0)

def is_character_printable(s):
    ## asciiの英数字・記号の文字列かどうかを判別し、真偽値を返します。
    if s < 126 and s >= 33:
        return True 

def print_headers():
    ## とりあえずフォーマット的なものを表示する
    print("")
    print("#### BINARY TO HEX DUMP - USING PYTHON3.6 ####")
    print("")
    print("Offset 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F Encode to ASCII")
    print("")

def validate_byte_as_printable(byte):
    ## ascii 文字列化をチェック. asciiでなければ '.' を返す ##
    if is_character_printable(byte):
        return byte
    else:
        return 46

def main():
    file_path = check_file_provided()
    memory_address = 0
    ascii_string = ""
    print_headers()



    ## 読み込んだバイナリファイルを表示し終わるまでループします
    for byte in read_bytes(file_path):
        ascii_string = ascii_string + chr(validate_byte_as_printable(byte))
        if memory_address%16 == 0:
            print(format(memory_address, '06X'),end = '')
            print(" " + hex(byte)[2:].zfill(2), end='')
        elif memory_address%16 == 15:
            print(" " + hex(byte)[2:].zfill(2),end='')
            print(" " + ascii_string)
            ascii_string = ""
        else:
            print(" " + hex(byte)[2:].zfill(2), end='')
        memory_address = memory_address + 1

if __name__ == '__main__':
    main()