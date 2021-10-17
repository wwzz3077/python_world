from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name = 'python_world',
    version = '0.0.1',
    author = 'wtzhao',
    autor_email = 'wtzhao@hotmail.com',
    description = ' a function that returns "world"',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = "https://github.com/wwzz3077/python_world",
    #packages = setuptools.find_packages(),
    keywords=['pip', 'package', 'wtzhao', 'python-world']
)
)