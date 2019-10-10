import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zeebe_grpc",
    version="0.21.1.1",
    author="Stéphane Ludwig",
    author_email="gitlab@stephane-ludwig.net",
    description="zeebe Python gRPC Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/stephane.ludwig/zeebe_python_grpc",
    packages=setuptools.find_packages(),
    install_requires=[
        'grpcio==1.24.1',
        'protobuf==3.10.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
