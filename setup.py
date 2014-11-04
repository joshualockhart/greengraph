from setuptools import setup, find_packages

setup(
    name = "GreenGraph",
    version = "0.2.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    install_requires = ['argparse', 'pypng', 'geopy', 'requests']
)
