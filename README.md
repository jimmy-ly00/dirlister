# DirLister

Generates wordlists to use for enumeration and brute-forcing files and directories. For example, you have discovered a web application that is running a certain CMS. First, find the source code and download it locally. Then use the tool to grab files, folders and/or extensions to generate wordlists used to force browse the application.

### Screenshots
![DirLister](https://i.imgur.com/eIGgDti.png  "Example usage of DirLister")

### Usage
Extract filenames and folders: `python dirlister.py -d sample`

Extract all formats :`python dirlister.py -d sample -o output`

```
root@kali:~# python DirLister.py -h
usage: DirLister.py [-h] [-d DIR] [-u URL] [-f {1,2,3,4,5}] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     Check a directory.
  -u URL, --url URL     Check a single URL.
  -f {1,2,3,4,5}, --format {1,2,3,4,5}
                        1= all, 2= folder names only, 3= filenames only, 4=
                        filenames without extensions, 5= extensions only
  -o OUTPUT, --output OUTPUT
                        Automatically saves all formats. Please specify a name
```

### TODO
- [ ] Support URLs such as GitHub API
- [ ] Add banner and pretty colours
