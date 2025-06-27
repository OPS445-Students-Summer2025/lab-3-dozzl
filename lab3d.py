#!/usr/bin/env python3
# Author ID: frajper


import os
import subprocess


def free_space():
    
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         shell=True, 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)

    output, error = p.communicate()

    
    return output.decode('utf-8').strip()


print(free_space())

