from setuptools import setup, find_packages
 	
import os
	 	
version = '0.1'
 	
setup(name='dimini.boilerplate',	 	
      version=version,	 	
      description="Dimini django-nonrel Google Appengine app as Python egg",	 	
      long_description="",
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Dimitri Roche',
      author_email='dimroc@gmail.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=["dimini"], 
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
