from setuptools import setup

def Readme():
    return open("README.md", "r").read()

setup(
    name = 'PyHttp',
    packages = ['pyhttp'],
    version = '0.1',
    description = Readme(),
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/pyhttp.git',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2'
    ],
    test_suite=['tests'],
    install_requires=[]
)