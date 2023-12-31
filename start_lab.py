#!/usr/local/bin/python3
# start_lab lab_number
import datetime
import sys
import pyperclip

print("diary LAB#.text")

if __name__ == "__main__":
    # Check argument
    if (len(sys.argv) != 2):
        print("Wrong number of arguments. Input lab number")
        sys.exit(1)
    labnum = sys.argv[1]

    clipboard = f"diary LAB{labnum}.text"
    clipboard +="""
% Yundi
% Xu
% m22als5-3
% """
    clipboard += datetime.date.today().strftime("%m/%d/%Y")
    print(clipboard)
    pyperclip.copy(clipboard)
