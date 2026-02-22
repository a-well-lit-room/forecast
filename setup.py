from setuptools import setup, find_packages

setup(
    name="forecast",
    version="0.1.0",
    description="Get a simple forecast for the next couple days.",
    author="a-well-lit-room",
    packages=find_packages(),
    install_requires=[
        "certifi==2026.1.4",
        "charset-normalizer==3.4.4",
        "idna==3.11",
        "requests==2.32.5",
        "urllib3==1.26.18"
    ],
    entry_points={
        "console_scripts": [
            "forecast=forecast.main:main",
        ],
    },
)
