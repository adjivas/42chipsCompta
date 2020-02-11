#!/usr/bin/env python

from pprint import pprint
import pyFarnell

f = pyFarnell.Farnell(apiKey='secret', region='fr.farnell.com')
pprint(f.get_part_number('2507703'))
