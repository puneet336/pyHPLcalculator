#!/usr/bin/env python
from __future__ import print_function
import argparse
import math


_parser=argparse.ArgumentParser()
_parser.add_argument("--nodes",'-n',required=True,help="number of nodes")
_parser.add_argument("--memory_size",'-m',required=True,help="size of memory in GB")
_parser.add_argument("--block_size",'-b',required=True,help="block size in grid")
_parser.add_argument("--memory_usage_percentage",'-u',required=True,help="block size in grid")
_parser.add_argument("--block_adjustment_factor",'-a',help="block size in grid")
_input_parameters=_parser.parse_args();

#calculate no. of DP elements
_n_dp_elements=( int(_input_parameters.nodes) *  int(_input_parameters.memory_size) *1024.0*1024.0*1024.0)/8.0

_problem_size=math.sqrt(_n_dp_elements)*( float(_input_parameters.memory_usage_percentage)/100.0)

#Align problem size to block size
_problem_size_aligned=(_problem_size/ int(_input_parameters.block_size))* int(_input_parameters.block_size)

#increase problem size!!
_problem_size_aligned=int(_problem_size_aligned+int(_input_parameters.block_adjustment_factor)*int(_input_parameters.block_size))


print("N=%d " %(_problem_size_aligned))
