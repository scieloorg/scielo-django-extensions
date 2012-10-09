from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''


setup(name='scielo-django-extensions',
      version='0.3.1',
      description='Extensions commonly used in SciELO for bibliographic metadata management.',
      packages=find_packages(),
      include_package_data=True,
      zip_safe = False,
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        ],
      keywords='SciELO Django Extensions',
      author='SciELO',
      author_email='scielo-dev@googlegroups.com',
      url='http://docs.scielo.org/',
      download_url='',
      license='',
      test_suite='scielo_extensions.tests',
      tests_require=['Nose'],
    )
