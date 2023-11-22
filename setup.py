from setuptools import setup, find_packages

setup(
    name="my_package",  # Replace with your package's name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",  # Since your assignment requires including pandas as a dependency
        # Add other dependencies if needed
    ],
    # Add other parameters as needed
)
