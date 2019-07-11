# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in security_management/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('security_management/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='security_management',
	version=version,
	description='Manage and monitor the security guard and gated community',
	author='utar',
	author_email='swsiong97@1utar.my',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
