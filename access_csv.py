#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import json
import csv

#
csv_file = pd.DataFrame(pd.read_csv("C:\\Users\\Steph\\Documents\\tblHaendler.txt", sep=";", header=0, index_col=False, encoding='latin-1'))
csv_file.to_json("C:\\Users\\Steph\\Documents\\json_file.json", orient="records", date_format="epoch", double_precision=10, force_ascii=False, date_unit="ms", default_handler=None)
data = json.load(open("C:\\Users\\Steph\\Documents\\json_file.json"))

with open("C:\\Users\\Steph\\Documents\\json_file.json", 'w') as outfile:
    json.dump(data, outfile, indent=4)

