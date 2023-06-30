from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Package Example'
LONG_DESCRIPTION = 'Package Example description.'

# Setting up
setup(
    name="package_example",
    version=VERSION,
    author="Krolik",
    author_email="<krolikpt@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)