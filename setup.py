from setuptools import setup, find_packages

version = "0.0.1"

setup(
    name="dataspace",
    packages=find_packages(),
    version=version,
    description="Diving equipment for data lake",
    author="synw",
    author_email="synwe@yahoo.com",
    url="https://github.com/synw/dataspace",
    download_url="https://github.com/synw/dataspace/releases/tag/" + version,
    keywords=["data_visualization", "data_exploration", "charts"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["pandas", "altair", "holoviews"],
    zip_safe=False,
)
