from setuptools import setup

def readme():
    with open('README.md', 'w') as f:
        return f.read()


setup(name='warrior_buddy',
      version='0.1',
      description="Fill me in",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Text Processing :: Linguistic',
          ],
      keywords='some string of keywords',
      url='git@github.com:john.martin/warrior_buddy.git',
      author='ClearDATA',
      author_email='YOUR.EMAIL@cleardata.com',
      license='MIT',
      packages=['warrior_buddy'],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
     )
