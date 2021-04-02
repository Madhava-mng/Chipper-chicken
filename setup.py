import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chipper-chicken",
    version="0.0.2",
    author="Madhava-mng",
    author_email="alformint@gmail.com",
    description="Cryptography chipper for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madhava-mng/Chipper-chicken",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['codelib'],
    python_requires='>=3.6',
)
