from CsvConverterBinary import *
from ArqProject import *
from structsArq import *
from operator import delitem
import pandas as pd
import numpy as np
import pickle
import os
import csv
import re

CsvtoBin()


trie1 = Trie()
trie1.insert("Brenda Galinha", 2001)
trie1.insert("Bruna", 2002)
trie1.insert("Pedro Bor", 2001)

print(trie1.starts_with("Br"))
