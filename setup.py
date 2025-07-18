from setuptools import setup, find_packages

setup(name='pip-test-package',
    version='0.1.1',
    author='PyPA',
    author_email='pypa@pypa.pypa',
    url='https://github.com/pypa',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': ['pip-test-package=piptestpackage:main'],
    },
    extras_require={
        'extra': ["simple"]
    },
)
