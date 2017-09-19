#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 ak73gucas, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: simple_code.py
Author: ak73gucas
Date: 2017/09/19 17:13:46
"""
import sys
import os
root = os.path.realpath(os.path.dirname(os.path.abspath(__file__)) + '/../')
sys.path.append(root)
from optparse import OptionParser
import logging

def parse_args():
    parser = OptionParser()
    parser.add_option('-i', '--infile', dest='input_file', default=None,
            help='input file. use default in config file.')
    parser.add_option('-o', '--outfile', dest='output_file', default=None,
            help='output file. use default in config file.')
    parser.add_option('-f', '--flag', dest='flag', default=True, action="store_true",
            help='flag. default is True.')
    parser.add_option('--log-level', dest='log_level', default='INFO', metavar='INFO',
            help='log level. default INFO')
    parser.add_option('--log-format', dest='log_format', default='[%(levelname)s] %(message)s',
            metavar='"[%(levelname)s] %(message)s"',
            help='log format. default "[%(levelname)s] %(message)s"')
    return parser.parse_args()

if __name__ == '__main__':
    opts, args = parse_args()
    logging.basicConfig(level=getattr(logging, opts.log_level), format=opts.log_format)
    print 'input_file: ', opts.input_file
    print 'output_file: ', opts.output_file
    print 'flag: ', opts.flag
    print 'log_level: ', opts.log_level
    print 'log_format: ', opts.log_format
