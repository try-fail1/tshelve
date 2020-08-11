import pathlib
import re
import setuptools


def get_version():
    local = pathlib.Path(__file__).parent / 'tshelve'/ '__init__.py'
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', local.read_text(), re.MULTILINE
    ).group(1)
    return version



def get_long():
    return (pathlib.Path(__file__).parent / 'README.rst').read_text()


setuptools.setup(
    name='tshelve',
    version=get_version(),
    description='A faster kind of Python shelf',
    long_description=get_long(),
    author='Ryan Vink',
    author_email='ryantvink@gmail.com',
    url='https://github.com/try-fail1/tshelve',
    keywords=['shelve', 'threads', 'threading', 'fileio', 'persistence'],
    python_requires='>=3.5',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Utilities'
    ]
)
