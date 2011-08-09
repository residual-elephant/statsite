from setuptools import setup

# Get the long description by reading the README
try:
    readme_content = open("README.rst").read()
except:
    readme_content = ""

setup(name='statsite',
      version='0.1.0-dev',
      description='Python statistics server which sends data to Graphite.',
      long_description=readme_content,
      author='Kiip',
      author_email='biz@kiip.me',
      maintainer='Kiip',
      maintainer_email='biz@kiip.me',
      url='https://github.com/kiip/statsite',
      keywords=['statsite', 'graphite', 'graph', 'metrics'],
      packages=['statsite'],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration"]
      )
