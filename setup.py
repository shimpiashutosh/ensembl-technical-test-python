from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ensembl-technical-test",
    version="1.0.0",
    author="Ashutosh Shimpi",
    author_email="ashutoshshimpi@gmail.com",
    description="Ensembl Technical Test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shimpiashutosh/ensembl-technical-test-python.git",
    packages=find_packages(),
    install_requires=["flask_restful==0.3.8", "flask==1.1.2", "pymysql==0.10.1",
                      "Werkzeug==1.0.1", "setuptools==51.0.0"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
