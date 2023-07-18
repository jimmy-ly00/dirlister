from setuptools import setup, find_packages

setup(
    name='dirlister',
    version='1.0.0', 
    python_requires='>=2.7',
    install_requires=['argparse; python_version==\'2.7\''],
    description='Generates wordlists to use for enumeration and brute-forcing files and directories',
    url='https://github.com/jimmy-ly00/dirlister',
    author='Jimmy Ly',
    author_email='jimmy-ly00@proton.me',
    license='GPL-2.0',
    packages=find_packages()+['.'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',  
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    entry_points={
        'console_scripts': [
            'dirlister = dirlister:interactive',
        ],
    },

)
