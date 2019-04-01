import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()
setuptools.setup(
	name='tsdeg',
	version='0.1',
	# scripts=['tsdeg'],  # this leads to a permissions error
	author="Matthew Moy de Vitry",
	author_email="matthew.moydevitry@eawag.ch",
	description="A tool to degrade time series data",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/mmmatthew/timeseries-degradation",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)