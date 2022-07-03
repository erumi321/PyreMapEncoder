"""Command-line interface for deppth functionality"""
import os
import argparse

from .pyre_map_encoder import encode_json

def main():
  parser = argparse.ArgumentParser(prog='pyre_map_encoder', description='Encode a JSON file into usable map binaries')
  subparsers = parser.add_subparsers(help='The action to perform', dest='action')

  # Pack parser
  pack_parser = subparsers.add_parser('encode', help='Encode JSON into a binary file', aliases=['ec'])
  pack_parser.add_argument('-i', '--input', metavar='input', default='input.thing_text', type=str, help='The JSON file to encode, default is input.thing_text')
  pack_parser.add_argument('-o', '--output', metavar='output', default='output.thing_bin', help='The binary file to output, default is output.thing_bin')
  pack_parser.set_defaults(func=cli_encode)

  args = parser.parse_args()
  args.func(args)

def cli_encode(args):
  input = args.input
  output = args.output

  encode_json(input, output)