#!/usr/bin/python
#
# Copyright 2012 Google Inc. All Rights Reserved.

"""Setup file for Earth Engine Python API package."""

try:
  # if setuptools is available, use it to take advantage of its dependency
  # handling
  from setuptools import setup                          # pylint: disable=g-import-not-at-top
except ImportError:
  # if setuptools is not available, use distutils (standard library). Users
  # will receive errors for missing packages
  from distutils.core import setup                      # pylint: disable=g-import-not-at-top

# check if the Python imaging libraries used by the mapclient module are
# installed, and print a warning
try:
  import ImageTk                                  # pylint: disable=unused-import,g-import-not-at-top
except ImportError:
  print """
    WARNING: A Python library (PIL) used by the Earth Engine API mapclient
    module was not found. Information on PIL can be found at:
    http://pypi.python.org/pypi/PIL
    """
try:
  import Tkinter                                  # pylint: disable=unused-import,g-import-not-at-top
except ImportError:
  print """
    WARNING: A Python library (Tkinter) used by the Earth Engine API
    mapclient module was not found. Instructions for installing Tkinter
    can be found at:
    http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter
    """

VERSION = '0.1.24'

setup(
    name='earthengine-api',
    version=VERSION,
    description='Earth Engine Python API',
    url='http://code.google.com/p/earthengine-api/',  # home page for package
    download_url='',  # package download URL
    packages=['ee'],
    package_data={
        'ee': [
            'tests/*.py',
        ],
    },
    test_suite='ee/tests',
    install_requires=[
        'google-api-python-client',
        'pyOpenSSL>=0.11',
    ],
    classifiers=[
        # Get strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='earth engine image analysis',
    author='Noel Gorelick',
    author_email='gorelick@google.com',
    long_description="""\
=======================
Earth Engine Python API
=======================
This package allows developers to interact with Google Earth Engine using the
Python programming language.
""",
)
