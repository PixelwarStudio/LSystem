from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="plant",
    version="0.1",
    description="",
    long_description=readme(),
    url="",
    author="Pixelwar",
    author_email="code@pxlwr.de",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
    ],
    license="MIT",
    packages=["plant"],
    zip_safe=False
)