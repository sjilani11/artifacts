from setuptools import setup

requires = [
    'pyramid',
    'plaster_pastedeploy',
    'pyramid_jinja2',
    'waitress',
'paste',
'requests'

]

setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
      py-modules = [],
)
