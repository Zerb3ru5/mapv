from setuptools import setup, find_packages

setup(
    name='mapv',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts':{
            'mapv = mapv.__main__:main'
        }
    }
)