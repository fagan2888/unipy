from setuptools import setup, find_packages


long_desc = """
This is made for some specific environment.
This contains some db connection tools & analysis tools. 
"""

setup(name='unipy',
	version='0.0.0.0.01',
	description='Useful tools for Analysis',
	long_description=long_desc,
	url='http://github.com/dawkiny',
	author='Young-Ju Kim',
	author_email='dawkiny@gmail.com',
	license='MIT License',
	classifiers=[
		# How Mature: 3 - Alpha, 4 - Beta, 5 - Production/Stable
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python :: 3.5'
		],
	packages=find_packages(exclude=['contrib', 'docs', 'tests']),
	install_requires=[
			  'pandas', 'numpy', 'scipy', 'statsmodels', 
				'pymysql', 'psycopg2', 'sqlalchemy',
				'ibm_db_sa' 
				#'cx_Oracle'
					],
	zip_safe=False)

