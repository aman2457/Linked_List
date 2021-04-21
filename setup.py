from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name = "py_linked_list",
    version = "0.0.1",
    description = "A Python package which contains some methods to manipulate a linked List.",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/aman2457/Linked_List",
    download_url = "https://github.com/aman2457/Linked_List/archive/refs/heads/main.zip",
    author = "Aman Kumar",
    author_email = "amankumar84349@gmail.com",
    license = "MIT",
    keywords = ["linked list", "list", "python linked list"],
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
    ],
    py_modules = ["Linked_List"],
    package_dir = {'': 'src'},
    include_package_data = True,
    install_requires = [],

)