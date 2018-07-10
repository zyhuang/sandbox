# -*- coding: utf-8 -*-

import os, sys, json


def qprint(msg):
    print(':: ' + msg, file=sys.stderr, flush=True)


def qopen(fname, mode='r', verbose=True):
    if verbose:
        if mode == 'w':
            qprint('writing {}'.format(fname))
        else:
            qprint('reading {}'.format(fname))

    return open(fname, mode)


def write_json(in_dict, out_json):

    fout = qopen(out_json, 'w')
    print(json.dumps(in_dict, sort_keys=True, indent=2), file=fout)
    fout.close()


def read_json(in_json):

    return json.loads(qopen(in_json).read())


def write_text(in_str, out_name):

    fout = qopen(out_name, 'w')
    print(in_str, file=fout)
    fout.close()


def read_text(in_name):

    return qopen(in_name).read()


# -------------------------------------------------------------------------

def play():

    import pygame
    pygame.init()
    pygame.mixer.music.load('bwv0529_bksn51sb.mid')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)

    pass




if __name__ == '__main__':

    play()


# end
