#!/usr/bin/python
# Author: Jimmy Ly
# Last Updated: 08/04/2018
import sys
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', dest='dir', help='Check a directory.', action='store')
    parser.add_argument('-u', '--url', dest='url', help='Check a single URL.', action='store')
    parser.add_argument('-f', '--format', dest='format', type=int,
                        help='1= all, 2= folder names only, 3= filenames only, 4= filenames without extensions, 5= extensions only',
                        default=1, choices=range(1,6), action='store')
    parser.add_argument('-o', '--output', dest='output', help='Automatically saves all formats. Please specify a name.', action='store')
    return parser.parse_args()

def walk(directory):
    files_original = list()
    dirs_original = list()
    for root, dirs, files in os.walk(directory):
        for dirname in dirs:
            dirs_original.append(dirname)
        for filename in files:
            files_original.append(filename)
    dirs_original = sorted(set(dirs_original))
    files_original = sorted(set(files_original))
    return (dirs_original,files_original)

def walk_url(url):
    print('Not supported yet')

def format_data(data, format):
    if format == 1:
        return('\n'.join(data[0]) + '\n' + '\n'.join(data[1]))
    if format == 2:
        return('\n'.join(data[0]))
    if format == 3:
        return('\n'.join(data[1]))
    if format == 4:
        final = list()
        for files in data[1]:
            temp = files.split('.')[0]
            final.append(temp)
        return('\n'.join(sorted(set(final))))
    if format == 5:
        final = list()
        for files in data[1]:
            temp = files.split('.')[1:]
            final.append('.'+'.'.join(temp))
        return('\n'.join(sorted(set(final))))

def output_file(data, output_filename):
    items = ('-all', '-folders', '-filenames', '-filenames-only', '-extensions')
    for index, item in enumerate(items, start=1):
        file = open(output + item + '.txt','w')
        file.write(format_data(data, index) + '\n')
    print('[-] Saved results to files')

def banner():
    print("")

def main(directory, url, format, output):
    if directory:
        data = walk(directory)
        print(format_data(data, format))
    elif url:
        print(url)
    if output:
        output_file(data, output)

def interactive():
    if len(sys.argv) <= 1:
        print('[*] DirLister - Generate wordlists from source codes.\n')
        #banner()
        print('Usage: python dirlister.py -d directory -o output')
        print('{} -h for help.'.format(sys.argv[0]))
        exit(0)

    args = parse_args()
    directory = args.dir
    url = args.url
    output = args.output
    format = args.format

    if args.dir is not None and args.url is not None:
        print('Please specify a directory folder (-d) or a URL (-u).\n Usage: python...')
        exit(0)

    try:
        main(directory, url, format, output)
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt Detected.\nExiting...')
        exit(0)

if __name__ == "__main__":
    interactive()