"""."""
from setuptools import setup


setup(
    name='rgbhex',
    package_dir={'': 'src'},
    py_modules=['rghhex'],
    author='Han Bao',
    author_email='hbao2016@hotmail.com',
    description='Given rgb format turn into hex code',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={'console_scripts': []}
)
