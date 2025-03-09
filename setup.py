from setuptools import setup, find_packages

setup(
    name='cicd-pipeline-monitor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask_restful',
        'requests',
        'matplotlib',
    ],
)