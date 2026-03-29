from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read()

setup(
    name="transformer_mt",
    version="1.0",
    packages=["transformer_mt"],
    install_requires=install_requires,
)