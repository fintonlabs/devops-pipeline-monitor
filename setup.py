from setuptools import setup, find_packages

setup(
    name='cicd-pipeline-monitor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'cicd-pipeline-monitor=main:main',
        ],
    },
)