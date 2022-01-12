from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in italy_compliance/__init__.py
from italy_compliance import __version__ as version

setup(
	name="italy_compliance",
	version=version,
	description="app to include lo compliance in Italy",
	author="Frappe Technologies",
	author_email="diksha@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
