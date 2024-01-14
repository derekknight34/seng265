#!/usr/bin/env python3
"""
Obtain and print the names of the packages without the cpu architecture (similar to A\installed4.py) that were installed within
the range of dates provided by the user (i.e., variables date_from and date_to). 

* Dates provided by the user should follow the format yyyy-mm-dd
* The output for each package belonging to the specified range should be:
yyyy-mm-dd: NAME_OF_PACKAGE
* An example of output from the program is described in range-2020-07-15-to-2020-07-16.txt

"""

import sys
import re


def main():

    if len(sys.argv) < 3:
        sys.exit(0)

    date_from = sys.argv[1]
    date_to   = sys.argv[2]

    line_number: int = 0

    # compiling the pattern first for best efficiency

    with open('dpkg.txt') as file:
        for line in file:
            line_number += 1
            m = re.compile(r"^(\d{4}-\d{2}-\d{2}).*")

            print(line)
            if m:
                print("%d: %s" % (line_number, m.group(2)))

if __name__ == "__main__":
    main()
