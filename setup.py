from setuptools import setup,find_packages



with open("README.md", "r") as txt:
    long_description = txt.read()
    
with open('requirements.txt') as f:
    to_install = f.read().split()
    

setup(
    name='PeakPxApi',
    version='1.0.0',
    description='get/search wallpapers from https://www.peakpx.com/',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='notstark',
    author_email='YeahAmStark@gmail.com',
    url='https://github.com/NotStark/PeakPX',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    install_requires=to_install, 
    python_requires='>=3.6'

)

