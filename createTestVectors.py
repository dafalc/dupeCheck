import os
import random
import string
import shutil


def createTestVectors(test_dir):

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