from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="published",
    version="0.1.0",
    packages=["published",],
    install_requires=[],
    license="MIT",
    url="https://pypi.org/project/published",
    author="python.supply",
    author_email="contact@python.supply",
    description="Example illustrating how an open-source library "+\
                "can be organized and published.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
