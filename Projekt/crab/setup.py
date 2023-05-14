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
        'PyPDF2',
    ],
    description='CRAB - compact REST Api backend',
    author=['Krzysztof Stefanski', 'Mateusz Setkowicz'],
    author_email=['kstefans@studnet.agh.edu.pl', 'setkowicz@studnet.agh.edu.pl'],
)