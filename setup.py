from setuptools import setup, find_packages
import os

version = 'trunk'

setup(
    name='pmr2.autoinc',
    version=version,
    description='Auto increment id provider',
    long_description=open('README.txt').read() + '\n' +
                     open(os.path.join('docs', 'HISTORY.txt')).read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
      ],
    keywords='',
    author='Tommy Yu',
    author_email='tommy.yu@auckland.ac.nz',
    url='',
    license='MPL, GPL, LGPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['pmr2'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
    )
