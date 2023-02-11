from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in item_translation/__init__.py
from item_translation import __version__ as version

setup(
	name="item_translation",
	version=version,
	description="Item Transalation",
	author="Vivek Thakor",
	author_email="vivekthakor1690@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
