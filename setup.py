from setuptools import find_packages, setup

setup(
    name='ebsdpy',
    packages=find_packages(
        include=['ebsdpy'],
        exclude=['tests']
    ),
    version='0.0.1',
    description='Medipix EBSD library',
    author='Nikolai Orlov',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
