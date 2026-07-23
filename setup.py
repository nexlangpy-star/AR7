from setuptools import setup, find_packages
import os

setup(
    name="AR7",
    version="1.3.7",
    packages=find_packages(),
    install_requires=[],
    author="devil",
    description="BETA 1.2",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_data={
        'AR7': ['*.so', 'python4'],
    },
    include_package_data=True,
    data_files=[
        ('bin', ['AR7/python4']),
        ('lib', ['AR7/libpython3.1N.so',"AR7/UR7.cpython-313.so"]),
    ],
    zip_safe=False,
)