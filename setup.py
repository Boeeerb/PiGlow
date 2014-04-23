from distutils.core import setup

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name	= 'PiGlow',
version	= '0.4',
author	= 'Jason Barnett',
author_email	= 'jase@boeeerb.co.uk',
description	= 'A module to control the PiGlow Raspberry Pi Addon Board',
long_description= 'A module to control the PiGlow Raspberry Pi Addon Board',
license	= 'MIT',
keywords	= 'Raspberry Pi PiGlow',
url	= 'http://www.boeeerb.co.uk',
classifiers = classifiers,
py_modules	= ['piglow'],
install_requires= ['rpi.gpio >= 0.5.4']
)