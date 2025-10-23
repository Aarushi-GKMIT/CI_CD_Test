from setuptools import setup, find_packages

setup(
    name="flask-ci-cd-demo",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "flask>=2.0.0",
        "pytest>=6.0.0",
        "gunicorn>=20.0.0",
    ],
)
