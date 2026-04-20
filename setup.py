from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-Jenkins",
    version="1.0",
    author="Kirtish Wankhedkar",
    packages=find_packages(),
    install_requires = requirements,
)