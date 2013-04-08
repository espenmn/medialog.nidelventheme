from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='medialog.nidelventheme',
      version=version,
      description="Nidelven Theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Theme Nidelven IT Grieg Medialog',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='http://medialog.no',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plonetheme.classic',
          'webcouturier.dropdownmenu',
          'wildcard.foldercontents',
          'medialog.portlet.placeholder',
          'Products.MenuNavigation',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
