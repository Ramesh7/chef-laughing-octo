from setuptools import find_packages
from setuptools import setup


setup(
    name='chef-laughing-octo',
    description='Pre commit hooks for chef development.',
    url='https://github.com/grizzly-monkey/chef-laughing-octo',
    version='v1.2',

    author='Jeet Parmar',
    author_email='jeet@coupa.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        # quickfix to prevent pep8 conflicts
        'flake8!=2.5.3',
        'argparse',
        'autopep8>=1.1',
        'pyyaml',
        'simplejson',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'check-cookstyle = octo-hooks.check_cookstyle:check_cookstyle',
            'check-rspec = octo-hooks.check_rspec:check_rspec',
            'check-foodcritic = octo-hooks.check_foodcritic:check_foodcritic',
        ],
    },
)
