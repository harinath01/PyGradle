from setuptools import setup, find_packages

requirements = ["ipython>=5.10.0", "requests>=2"]

setup(
    name="helloworld",
    version="0.0.1",
    author="hari",
    author_email="hari@testpress.in",
    description="A package",
    long_description="readme",
    long_description_content_type="text/markdown",
    url="https://github.com/testpress/testpress_python/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)