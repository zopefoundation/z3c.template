##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup

$Id$
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup (
    name='z3c.template',
    version = '1.2.1',
    author = "Roger Ineichen and the Zope Community",
    author_email = "zope-dev@zope.org",
    description = "A package implementing advanced Page Template patterns.",
    long_description=(
        read('README.txt')
        + '\n\n.. contents::\n\n'+
        read('src', 'z3c', 'template', 'README.txt')
        + '\n' +
        read('src', 'z3c', 'template', 'zcml.txt')
        + '\n' +
        read('CHANGES.txt')
        ),
    license = "ZPL 2.1",
    keywords = "zope3 template layout zpt pagetemplate",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
    url = 'http://pypi.python.org/pypi/z3c.template',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    namespace_packages = ['z3c'],
    extras_require = dict(
        test = ['zope.app.testing',
                'zope.testing',
                'lxml>=2.1.1',
                'z3c.pt>=1.0b1'],
        ),
    install_requires = [
        'setuptools',
        'zope.component',
        'zope.configuration',
        'zope.interface',
        'zope.pagetemplate',
        'zope.publisher',
        'zope.schema',
        'z3c.ptcompat [zpt]',
        ],
    include_package_data = True,
    zip_safe = False,
    )
