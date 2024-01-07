"""
Setup script for installing this package.
"""

from setuptools import setup, find_packages

# Load README
with open('README.md') as README_md:
    README = README_md.read()

setup(
    name='gym_super_mario_bros_3',
    version='0.0.1',
    description='Super Mario Bros. 3 for Gymnasium',
    long_description=README,
    long_description_content_type='text/markdown',
    keywords=' '.join([
        'OpenAI-Gym',
        'Farama-Foundation-Gym',
        'NES',
        'Super-Mario-Bros-3',
        'Reinforcement-Learning-Environment',
    ]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: Free For Educational Use',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    url='https://github.com/voacado/gym-super-mario-bros-3',
    author='A Vo',
    author_email='vo.ant@northeastern.edu',
    # license='Proprietary',
    # packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    # package_data={'gym_super_mario_bros_3': ['_roms/*.nes']},
    install_requires=['nes-py @ git+https://github.com/ItaiBear/nes-py@gymnasium'],
    entry_points={
        'console_scripts': [
            'gym_super_mario_bros = gym_super_mario_bros._app.cli:main',
        ],
    },
)

# TODO: Finish setup.py