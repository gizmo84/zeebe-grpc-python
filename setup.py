import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zeebe_grpc",
    version="0.20.0.4",
    author="Stéphane Ludwig",
    author_email="gitlab@stephane-ludwig.net",
    description="zeebe Python GRPC Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/stephane.ludwig/zeebe_python_grpc",
    packages=setuptools.find_packages(),
    install_requires=[
        'grpcio==1.22.0',
        'protobuf==3.9.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
