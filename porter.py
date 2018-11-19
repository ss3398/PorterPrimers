#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Hackathon2 Porter Primers')
parser.add_argument('-s','--input',help='input file',required=True)
parser.add_argument('-p','--primer',help='primers file',required=True)

args = vars(parser.parse_args())

print "input given" + args['input']
print "primer given" + args['primer']
print "hello argparse"
