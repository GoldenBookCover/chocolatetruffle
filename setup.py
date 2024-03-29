import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chocolatetruffle",
    version="1.3.1",
    author="Monstre Charmant",
    author_email="ballonrage@gmail.com",
    description="Useful sysadmin tool-kit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MonstreCharmant/chocolatetruffle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
