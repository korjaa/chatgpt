import os
from setuptools import setup, find_packages

pkg_name = "chatgpt"

# Get version
exec(open(os.path.join(pkg_name, "version.py")).read())

setup(
    name=pkg_name,
    version=__version__,
    url=f"https://github.com/korjaa/{pkg_name}",
    author="Jaakko Korhonen",
    author_email="user@email.com",
    description="ChatGPT commandline chat",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            f"chatgpt={pkg_name}.assistant:main",
            f"cargpt={pkg_name}.mechanic:main"
        ]
    },
    install_requires=[
        "openai==0.27.6"
    ],
)
