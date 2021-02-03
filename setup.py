import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-dpi-aware",
    version="0.0.1",
    author="ElectronicElephant",
    author_email="imtangtt@outlook.com",
    description="Set the DPI Awareness for your Python program on Windows platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElectronicElephant/py_dpi_aware",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
