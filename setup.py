from setuptools import setup, find_packages


scripts = []
version = 0.1

setup(
    name="axe",
    version=version,
    packages=find_packages(),
    scripts=scripts,
    include_package_data=True,
    zip_safe=False,
    # include_package_data = True,    # include everything in source control
    # exclude_package_data = { '': ['README.txt'] },
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['pymysql', 'MySQL-python'],
    # packages=['src'],
    package_data={
        'doc': ['*.txt'], 'xml': ['*.xml', 'relax/*.rnc'],
        # If any package contains *.txt or *.rst files, include them:
        #'': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        #'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Kenny Zhang",
    author_email="sphy@foxmail.com",
    description='',
    license="BSD",
    keywords="database pool",
    url="https://github.com/philoprove/axe",
    # could also include long_description, download_url, classifiers, etc.
)
