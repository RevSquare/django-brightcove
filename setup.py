#! /usr/bin/env python
from distutils.core import setup
from setuptools import find_packages
import sys
reload(sys).setdefaultencoding('Utf-8')


setup(
    name='django-brightcove',
    version='0.0.3',
    author='Guillaume Pousseo',
    author_email='guillaumepousseo@revsquare.com',
    description='Manages integration of brightcove into django.',
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
    ],
    install_requires=[
        'Django>=1.4',
        'brightcove>=0.2',
    ],
)
