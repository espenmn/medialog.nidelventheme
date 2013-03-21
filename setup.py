from setuptools import setup, find_packages
import os

version = '0.1'

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
      keywords='Plone Theme Kongsberg',
      author='EMN',
      author_email='espen@medialog.no',
      url='http://svn.plone.org/svn/collective/',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nidelven'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plonetheme.classic',
          'webcouturier.dropdownmenu',
          'wildcard.foldercontents',
          'medialog.portlet.placeholder',
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
