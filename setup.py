#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="compta42chips",
    version="1.0.0",
    packages=["compta42chips"],
    package_data={
        "compta42chips": ["*.csv"],
    },
    scripts = ["compta42chips/compta42chips.py"],
    install_requires = [
        "pyFarnell",
        "docopt",
    ],
    author="adjivas",
    author_email="adjivas@users.noreply.github.com",
    maintainer="adjivas",
    maintainer_email="adjivas@users.noreply.github.com",
    keywords=[""],
    description="""remplit une demande de dépense 42.""",
    long_description="",
    include_package_data=True,
    url="https://adjivas.github.io/compta42chips",
    platforms=["any"],
    classifiers=[
        "Environment :: Console",
        "Operating System :: Unix",
    ],
    license="GPL-3",
}
