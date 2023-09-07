import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


__version__ = "0.0.0"
REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "prasanth1729"
SRC_REPO = "cnnclassifier"
AUTHOR_EMAIL = "prasanthdowtya@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python  package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
