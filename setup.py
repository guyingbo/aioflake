try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os.path
import re
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
BASE_PATH = os.path.dirname(__file__)


with open(os.path.join(BASE_PATH, 'aioflake.py')) as f:
    try:
        version = VERSION_RE.search(f.read()).group(1)
    except IndexError:
        raise RuntimeError('Unable to determine version.')


setup(
    name='aioflake',
    description="Unique id generator inspired by twitter's snowflake.",
    license='MIT',
    version=version,
    author='Yingbo Gu',
    author_email='tensiongyb@gmail.com',
    maintainer='Yingbo Gu',
    maintainer_email='tensiongyb@gmail.com',
    url='https://github.com/guyingbo/aioflake',
    py_modules=['aioflake'],
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
