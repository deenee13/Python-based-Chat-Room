#!/usr/bin/python

import argparse

def helper_parse_argument(data_dict):
    parser = argparse.ArgumentParser()
    for key, value in data_dict.items():
        if value[1] == "str":
            parser.add_argument(key, value[0], type=str)
        elif value[1] == "int":
            parser.add_argument(key, value[0], type=int)
        elif value[1] == "float":
            parser.add_argument(key, value[0], type=float)

    return parser.parse_args()
