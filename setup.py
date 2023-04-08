from setuptools import setup

readme = ''

with open('README.md', encoding="utf8") as f:
    readme = f.read()
    
with open('requirements.txt') as f:
    to_install = f.read().split()
    
    
setup(
    name='Peakpx',
    author='NotStark',
    author_email='YeahAmStark@gmail.com',
    version='1.0.0',
    long_description=readme,
    url='https://github.com/NotStark/PeakPX',
    packages=['Peakpx'],
    classifiers=[
        'Intended Audience :: Developers',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    description='get/search wallpapers from https://www.peakpx.com/',
    include_package_data=True,
    keywords=['peakpx','notstark'],
    install_requires= to_install 

)
