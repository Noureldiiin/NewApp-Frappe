from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nourapp/__init__.py
from nourapp import __version__ as version

setup(
	name="nourapp",
	version=version,
	description="new app",
	author="Nour",
	author_email="nour.eldin06@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
