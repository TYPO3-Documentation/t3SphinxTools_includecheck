from __future__ import absolute_import
from setuptools import setup

setup(name='t3sphinxtools_includecheck',
      version='1.0',
      description='Check file paths of included reST files',
      url='http://github.com/TYPO3-Documentation/t3SphinxTools_checkincludes',
      author='Martin Bless',
      author_email='martin.bless@mbless.de',
      license='MIT',
      packages=['t3sphinxtools_includecheck'],
      zip_safe=False,
      scripts=['t3sphinxtools_includecheck/check_include_files.py'])
