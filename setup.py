import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="change_calculator", # Replace with your own username
    version="1.0.0",
    author="Jeremy Pollard",
    author_email="email.pollard@gmail.com",
    description="A component to calculate change from a given set of coins.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)