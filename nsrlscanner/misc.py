""" NSRLScanner Misc Functions"""
import os
import sys


def generate_file_list(root):
    """Generate file traversal list to scan

        :arg root: root direcotry of filesystem to
            add to scan path

        :returns array of file locations
    """
    file_array = []
    for root, dirs, files in os.walk(root):
        for file in files:
            file_array.append(os.path.join(root,file))

    if len(file_array) == 0:
        print("[!] Error: No files Found in specified path. Exiting.")
        sys.exit(1)
    return file_array
