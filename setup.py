import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "m360",
    version = "0.0.1",
    author = "Jaya Balan Aaron",
    author_email = "bucket.size@gmail.com",
    description = "monitor stuff",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux',
    ],
    packages = ['m360'
                , 'm360.config'
                , 'm360.fragments'
                , 'm360.interfaces'
                , 'm360.writers'
                ],
    scripts = ['bin/m360'],
    include_package_data=True,
    python_requires = ">=3.6"
)
