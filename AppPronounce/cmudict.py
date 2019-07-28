import sys
import os
import re
import codecs
from .cmuToKorean import CMUToKorean

def fUpper(match):
    return match.group(0).upper()

def DisplayCMU(tofind):
    result = []
    filename = os.path.abspath('AppPronounce/cmudict-0.7b.txt')
    if not os.path.exists(filename):
        print('No dictionary file: %s' % filename)
        sys.exit()
    f = codecs.open(filename, 'r', encoding='utf8')
    cmudict = f.read()
    f.close()

    tstr = tofind.strip()

    for tstr in tstr.split():
        # find input word in CMU dict
        keyword = re.sub('[\[\]]', '', tstr)
        keyword = re.sub('[a-zA-Z]+', fUpper, keyword)
        regexEpr = r"\n" + keyword + r"  (.+)\n"
        match = re.search(regexEpr, cmudict)
        if match == None:
            print(tstr)
            continue

        # convert its pronunciation into Korean
        results = CMUToKorean.convert(tstr, match.group(1))
        result.append(results[0])
    
    return result
