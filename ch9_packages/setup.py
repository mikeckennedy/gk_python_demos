# from distutils.core import setup
from setuptools import setup

setup(
    name='sports',
    version='0.1',
    packages=['sports', 'sports.extras'],
    requires=['requests'],
    url='http://google.com?search=olympics',
    license='MIT',
    author='Administrator',
    author_email='a@admin.com',
    description='The description'
)
