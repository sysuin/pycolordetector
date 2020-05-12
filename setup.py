from setuptools import find_packages, setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pycolordetector',
      packages=find_packages(include=['pycolordetector']),
      version='0.0.1',
      description='A simple library for detecting colors in images',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Sunny Singh',
      author_email='sunnysinghnitb@gmail.com',
      license='MIT',
      url='https://github.com/sunnysinghnitb/pycolordetector',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      project_urls={
        'Documentation': r'https://pycolordetector.readthedocs.io/en/latest/'
      },
      )
