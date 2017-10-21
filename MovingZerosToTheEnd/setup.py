"""."""
from setuptools import setup


setup(
    name='movezeros',
    package_dir={'': 'src'},
    py_modules=['movezeros'],
    author='Han Bao',
    author_email='hbao2016@hotmail.com',
    description='Given a list of random type objects, return a list with the int zeros at the end of list',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={'console_scripts': []}
)
