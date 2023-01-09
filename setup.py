from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Prakhar2295",
    description="A small package for DVC ML PROJECT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Prakhar2295/MLOPS_MOBILE-_PRICE_PREDICTION.git",
    author_email="prakhar.kumar5@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)