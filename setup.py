from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name = "Linked_List",
    version = "0.1.0",
    description = "A Python package to work with LinkedList.",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/aman2457/Linked_List",
    download_url = "https://github.com/aman2457/Linked_List/archive/refs/heads/main.zip",
    author = "Aman Kumar",
    author_email = "",
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