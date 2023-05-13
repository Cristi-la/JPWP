from setuptools import setup, find_packages

setup(
    name='crab',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'crab=crab.cli.main:run',
        ],
    },
    include_package_data=True,
    install_requires=[
        # list dependencies here
    ],
    description='CRAB - compact REST Api backend',
    author='test',
    author_email='kstefans@studnet.agh.edu.pl',
)