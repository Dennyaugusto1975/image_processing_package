from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.3",
    author="Denny",
    author_email="denny.augusto1975@gmail.com",
    description="Processamento de imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dennyaugusto1975/image_processing_packpages",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)