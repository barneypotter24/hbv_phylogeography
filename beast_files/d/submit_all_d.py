import os
import shutil
import subprocess

files = os.listdir('.')

for file in files:
    if file.endswith('.pbs'):
        command = ['qsub', file]
        print(" ".join(command))
        try:
            subprocess.call(command)
        except:
            print("failed to submit")
        number = file.split('_')[1].split('.')[0]
        print("mv {} {}/{}".format(file, number, file))
        try:
            shutil.move(file, "{}/{}".format(number,file))
        except:
            print("failed to move")
