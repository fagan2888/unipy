#-*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:55:26 2017

@author: Young Ju Kim
"""

try:

    from setuptools import setup, find_packages

except ImportError:

    from distutils.core import setup, find_packages


import tarfile


def package_data_listup():

    filename = 'sample/datasets/resources.gz/resources.tar.gz'
    tar = tarfile.open(filename)
    filelist = list(set(map(lambda x: x.split('/')[0], tar.getnames())))
    filelist.sort()
    return filelist


long_desc = """
This is made for some specific environment.
This contains codes for data manipulation and Analysis tools.
"""

setup(name='unipy',
      version='0.0.1.49',
      description='Useful tools for Data Scientists',
      long_description=long_desc,
      url='http://github.com/pydemia/unipy',
      author='Young Ju Kim',
      author_email='pydemia@gmail.com',
      license='MIT License',
      classifiers=[
            # How Mature: 3 - Alpha, 4 - Beta, 5 - Production/Stable
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Programming Language :: Python :: 3.5',
            'Operating System :: OS Independent',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Natural Language :: English',
            ],
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=[
                        'pandas', 'numpy', 'scipy', 'statsmodels',
                        'pymysql', 'psycopg2', 'sqlalchemy',
                        'ibm_db_sa'
                        # 'cx_Oracle'
                        ],
      zip_safe=False,
      package_data={'unipy': ['*.gz', 'sample/datasets/resources.tar.gz']}
      )
