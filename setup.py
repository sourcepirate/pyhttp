from setuptools import setup

import os


def Readme():
    return open(os.path.join(os.path.dirname(__file__), 'README.md'), "r").read()

setup(
    name='pyrequest',
    packages=['pyhttp'],
    version='0.5',
    description='Pythonic way of HTTP request',
    long_description = Readme(),
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/pyhttp.git',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers'
    ],
    install_requires = ['urllib3', 'certifi'],
    include_package_data=True,
    license='MIT License',
)