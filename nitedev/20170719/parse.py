# -*- coding: utf-8 -*-

import os, sys, json, re

def pileup_parser(pu_str):

    tmp = re.findall(r'(\^.[\.,a-zA-Z]|.\$|[\.,][\+\-]\d+[a-zA-Z]+\$?|[\*\.,a-zA-Z])', pu_str)
    pu_list = []
    for x in tmp:
        if re.findall(r'[\.,][\+\-]', x):
            prefix, nbp, suffix = re.findall(r'([\.,][\+\-])(\d+)(.*?)$', x)[0]
            nbp_int = int(nbp)
            pu_list.append(prefix + nbp + suffix[:nbp_int])
            for c in suffix[nbp_int:]:
                if c != '$':
                    pu_list.append(c)
                else:
                    pu_list[-1] += '$'
        else:
            pu_list.append(x)

    if pu_str != ''.join(pu_list):
        print('*ERROR* pileup list can not reproduce pileup string:\n<< {}\n>>{}'
              .format(pu_str, ''.join(pu_list)), file=sys.stderr)

    return pu_list


def parse(in_file, out_file):

    fout = open(out_file, 'w')
    nline = 0
    print(':: Reading {}'.format(in_file))
    for line in open(in_file):
        nline += 1
        data = line.rstrip().split('\t')

        pu_list = pileup_parser(data[4])
        print('<<', data[0], data[1], data[4], file=fout)
        print('>>', pu_list, file=fout)
        if int(data[3]) != len(pu_list):
            print('*WARNING* different number of reads: expected {}, parsed {}, input line:\nLine{}: {} ...'
                  .format(int(data[3]), len(pu_list), nline, line.rstrip()[:100]), file=sys.stderr)

        if data[7] != '0':
            pu_list = pileup_parser(data[8])
            print('<<', data[0], data[1], data[8], file=fout)
            print('>>', pu_list, file=fout)
            if int(data[7]) != len(pu_list):
                print('*WARNING* different number of reads: expected {}, parsed {}, input line: #{}\nLine{}: {} ...'
                      .format(int(data[7]), len(pu_list), nline, line.rstrip()[:100]), file=sys.stderr)
    fout.close()
    print(':: Output written to {}'.format(out_file))

if __name__ == '__main__':

    in_file, out_file = sys.argv[1:3]
    parse(in_file, out_file)


# end
# ty to Zhuoyi
