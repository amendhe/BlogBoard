from setuptools import find_packages, setup
'''
This tells Python to copy everything in the static and 
templates directories, and the schema.sql file, 
but to exclude all bytecode files.
'''
setup(
    name='Notice_Board',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)