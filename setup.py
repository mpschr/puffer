from setuptools import setup, find_packages

requires_list = [
    'colorama==0.2.7',
    'coverage==3.7.1',
    'mock==1.0.1',
    'nose==1.3.0',
    'rauth==0.7.2',
    'requests==2.10.0',
]

setup(name='puffer',
      version='1.8.2',
      platforms='any',
      description='Python wrapper for the Buffer API',
      author='Vlad Temian, Victor Villas',
      author_email='villasv@outlook.com',
      url='https://github.com/villasv/puffer',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires_list,
      classifiers=[
          'Programming Language :: Python :: 3.5'
      ]
      )
