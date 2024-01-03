from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='BulkFileOperationsManager',
    version='0.0.4',
    description='Python package for managing bulk file CRUD operations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    url='https://github.com/chigwell/BulkFileOperationsManager',
    packages=find_packages(),
    install_requires=[
        'filechunkcrud'
    ],
)
