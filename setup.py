from setuptools import setup

setup(
	name='fourier',
	version='0.1',
	packages=['fourier',],
	install_requires=[
            'matplotlib',
			'numpy',
			'scipy'
        ],
	license='Creative Commons Attribution-Noncommercial-Share Alike license',
	long_description=open('README.md').read()
	)

