from setuptools import setup
setup(
    name='checkblock',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'checkblock=blockjob:run'
        ]
    }
)
