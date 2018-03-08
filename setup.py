from setuptools import setup

setup(
    name="LindenmayerSystem",
    version="0.1",
    description="A implementation of Lindenmayer systems including context sensitive and probalistic variation.",
    url="",
    author="Pixelwar",
    author_email="code@pxlwr.de",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=[
        "attr"
    ],
    license="MIT",
    py_modules=["lsystem"],
    zip_safe=False
)