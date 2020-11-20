import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name='safecustody_sdk',
      version='1.0.5',
      description='safecustody wallet api sdk',
      author='wangxudong',
      author_email='834971685@qq.com',
      url='https://github.com/chainlife-doc/safecustody_sdk_python',
      packages=setuptools.find_packages(),
      python_requires='>=3.6',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      )
