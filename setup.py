#!/usr/bin/env python
from setuptools import setup
from os.path import dirname, join

import market_maker

here = dirname(__file__)

setup(name='bitmex-market-maker',
      version=market_maker.__version__,
      description='Market making bot for BitMEX API',
      url='https://github.com/martin-juul/sample-market-maker',
      long_description=open(join(here, 'README.md')).read(),
      long_description_content_type='text/markdown',
      author='Martin Juul',
      author_email='code@juul.xyz',
      install_requires=[
          'requests',
          'websocket-client',
          'future'
      ],
      packages=['market_maker', 'market_maker.auth', 'market_maker.utils', 'market_maker.ws'],
      entry_points={
          'console_scripts': ['marketmaker = market_maker:run']
      }
      )
