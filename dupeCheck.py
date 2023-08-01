import os
import hashlib
import sqlite3
import string
import random
import shutil
import sys
import inspect

import sqlalchemy
import pandas as pd

# script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
# script_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# script_directory = os.path.realpath(os.path.dirname(__file__))
# test_dir = script_directory + "\\test_files"

proj_dir = "C:\\Users\\falco\\src\\duplicate_finder"
test_dir = "C:\\Users\\falco\\src\\duplicate_finder\\test_files"

# Create test files with some duplicates

os.chdir(r"test_dir")

fileSizeInBytes = 1024

N = 7
for i in range(10):
    output_filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    with open(output_filename, 'wb') as fout:
        fout.write(os.urandom(fileSizeInBytes)) # replace 1024 with a size in kilobytes if it is not unreasonably large
    if random.random() % 2:
        shutil.copyfile(output_filename, ''.join(random.choices(string.ascii_uppercase + string.digits, k=N)))


dict = {'File Name':[],
        'Checksum':[]
        }

df = pd.DataFrame(dict)

# Generate checksums and put them in a DataFrame
os.chdir(test_dir)

for root, dirs, files in os.walk(".", topdown = False):
    
        for name in files:
            print(os.path.join(root, dirs, name))

            with open(name, 'rb') as file_to_check:
                data = file_to_check.read()
                md5_returned = hashlib.md5(data).hexdigest()
            
            print(md5_returned)

            df.loc[len(df.index)] = [name, md5_returned] 

pd.display(df)

group = df.groupby('Checksum')['File Name'].unique()
group[group.apply(lambda x: len(x)>1)]
group

# os.chdir(r"..")
con = sqlite3.connect("checksums.db")
cur = con.cursor()
cur.execute(CREATE TABLE dirpath, dirname, filename)