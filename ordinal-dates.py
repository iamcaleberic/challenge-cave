#!/usr/bin/env python3
# output the dates in a format
    # YYYY - MM - D
    # challenge is ordinal dates are not supported in some languages
    # and you are not allowed to use libraries so we use the python stdlib
    
import re
from datetime import datetime

def main():
    d_array = ["30th May 2019", "12th June 2012", "14th July 1993", "30th July 1994", "1st January 2020", "2nd May 1912"]
    for d_ in d_array:
        date_string = re.sub(r'(th|nd|st)', "", d_)
        parsed_date = datetime.strptime(date_string, "%d %B %Y")
        print(parsed_date.strftime("%Y-%m-%d")
)

if __name__ == '__main__':
    main()
