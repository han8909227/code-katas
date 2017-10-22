"""."""
from setuptools import setup


setup(
    name='parameter_of_squares',
    package_dir={'': 'src'},
    py_modules=['parameter_of_squares'],
    author='Han Bao',
    author_email='hbao2016@hotmail.com',
    description='The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={'console_scripts': []}
)
