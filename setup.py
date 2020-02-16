import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stockpy",
    version="0.0.1",
    author="chaosxu",
    author_email="chaosxu@foxmail.com",
    description="a simple stock analysis libarary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chaosxu/stockpy",
    packages=setuptools.find_packages(include=('./stockpy/**/*')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
