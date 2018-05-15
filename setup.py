from setuptools import setup, find_packages

setup(
    name='dukedoms-card-broker-component-tests',
    version='0.1.0',
    description='containerized testing environment for dukedoms card broker',
    packages=find_packages(exclude=['&.tests']),
    install_requires=[
        'addict',
        'behave',
        'bravado',
        'sqlalchemy',
        'psycopg2',
        'pyhamcrest'
    ]
)
