from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='redmine-auth',
      version=version,
      description="An apache2 authentication provider implementation, redmine database used to authenticate. It can be used for subversion authentication, etc.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='apache, apache2, redmine, auth, svn, subversion',
      author='LaiYonghao',
      author_email='mail@laiyonghao.com',
      url='https://github.com/laiyonghao/redmine-auth',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'argparse',
          'web.py',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      redmine-auth = redmineauth.main:main
      """,
      )
