"""."""
from setuptools import setup


setup(
    name='sum_of_nth_series',
    package_dir={'': 'src'},
    py_modules=['sum_of_nth_series'],
    author='Han Bao',
    author_email='hbao2016@hotmail.com',
    description='Find the sum of a series up to the nth term',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={'console_scripts': []}
)
