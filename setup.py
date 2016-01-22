from setuptools import setuptools

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name="qqlolapi",
    version="0.1",
    description="Wrapper for QQ LoL Esports Data API",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="api bindings lol qq china esports data scoreboard wrapper",
    url="http://github.com/flakeee/qqlolapi",
    author="Flake",
    author_email="flake@anio.xyz",
    license="LGPLv3",
    packages=["qqlolapi"],
    install_requires=["requests>=2.9.1", "pytz>=2015.7"],
    include_package_data=True,
    zip_safe=False,
)