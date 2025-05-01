import ast
from setuptools import setup, find_packages


def find_version():
    with open('parser/__init__.py', encoding='utf-8') as fp:
        result = ast.parse(fp.read())
        for item in result.body:
            if not isinstance(item, ast.Assign):
                continue
            
            for target in item.targets:
                if getattr(target, 'id') != '__version__':
                    continue
                
                return item.value.value


setup(
    name='parser',
    version=find_version(),
    author='milad',
    description='A lightweight LALR parser and lexer framework.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mivmi/lalr-parser',
    project_urls={
        'Source Code': 'https://github.com/mivmi/lalr-parser',
        'Bug Tracker': 'https://github.com/mivmi/lalr-parser/issues'
    },
    license='MIT',
    packages=find_packages(),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6'
)
