#-*- coding: utf-8 -*-
"""
Created on 2017-01-05 20:55:26
Modified on 2017-06-26 02:36:25

@author: Young Ju Kim
"""


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import tarfile


_version = '0.0.3.21'



def package_data_listup():

    filename = 'dataset/resources.gz/resources.tar.gz'
    tar = tarfile.open(filename)
    filelist = list(set(map(lambda x: x.split('/')[0], tar.getnames())))
    filelist.sort()
    return filelist


long_desc = """
This is made for some specific environment.
This contains codes for data manipulation and Analysis tools.
"""

required_packages = [
                     'pandas >= 0.20.1',
                     'numpy >= 1.13.1',
                     'scipy >= 0.19.1',
                     'scikit-learn >= 0.18.0',
                     'statsmodels >= 0.8.0',
                     'matplotlib >= 2.0.2',
                     'paramiko >= 2.1.2',
                     'pandasql >= 0.7.3',
                     'seaborn >= 0.8',
                     'scikit-image >= 0.13.0',
                     #'pyqt5',
                     'mglearn >= 0.1.6',
                     'numba >= 0.34.0',
                    # 'nomkl',  # conda
                    ]


with open('REQUIREMENTS.txt', 'w') as f:
    header = '--index-url https://pypi.python.org/simple/'
    pkg_ls = '\n'.join(required_packages).replace('>=', '==')
    f.write('\n'.join([header, pkg_ls]))


setup(name='unipy',
      version=_version,
      description='Useful tools for Data Scientists',
      long_description=long_desc,
      url='http://github.com/pydemia/unipy',
      author='Young Ju Kim',
      author_email='pydemia@gmail.com',
      license='MIT License',
      classifiers=[
            # How Mature: 3 - Alpha, 4 - Beta, 5 - Production/Stable
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Operating System :: OS Independent',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Natural Language :: English',
            ],
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      #setup_requires=required_packages,
      install_requires=required_packages,
      zip_safe=False,
      package_data={'unipy': ['*.gz', 'dataset/resources.tar.gz']}
      )


