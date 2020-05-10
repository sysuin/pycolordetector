from setuptools import find_packages, setup

setup(name='pycolordetector',
      packages=find_packages(include=['pycolordetector']),
      version='0.0.1',
      description='A simple library for detecting colors in images',
      author='Sunny Singh',
      author_email='sunnysinghnitb@gmail.com',
      url='https://github.com/sunnysinghnitb/pycolordetector',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      )