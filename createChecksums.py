import os
import hashlib

import pandas as pd



def createChecksums(test_dir):

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