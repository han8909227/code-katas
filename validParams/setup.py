"""."""
from setuptools import setup


setup(
    name='valid_params',
    package_dir={'': 'src'},
    py_modules=['valid_params'],
    author='Han Bao',
    author_email='hbao2016@hotmail.com',
    description='Given a string of paramticies, determine if they have been closed properly(i.e valid)',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={'console_scripts': []}
)
