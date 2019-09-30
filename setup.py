from setuptools import setup

setup(name='csci587hw1viz',
      version='0.1',
      author='Frank Greguska',
      author_email='greguska@usc.edu',
      license='MIT',
      packages=['csci587hw1viz'],
      install_requires=[
          'pandas',
          'descartes',
          'geopandas',
          'matplotlib',
          'folium'
      ],
      zip_safe=False)
