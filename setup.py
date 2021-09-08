import setuptools

setuptools.setup(
    name="excel_scraper",
    version="0.0.3",
    author="aeorxc",
    description="Utility library to scrape timeseries data from excel files",
    url="https://github.com/aeorxc/excel-scraper",
    project_urls={
        "Source": "https://github.com/aeorxc/excel-scraper",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "openpyxl"],
    python_requires=">=3.8",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
