from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='RPCGeoTag2RPCTxt',
    version='0.0.1',
    author="Saif Aati",
    author_email="saif@caltech.edu, saifaati@gmail.com",
    description="Extract RPCs from raster metada (tif,jp2,Ntif) to txt file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SaifAati/RPCGeoTag2RPCTxt.git',
    python_requires='>=3.5',
     classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    packages=['RPCGeoTag2RPCTxt',], 
)
