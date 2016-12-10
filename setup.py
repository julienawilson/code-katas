"""The setup for my code-katas distrobution."""

from setuptools import setup

setup(
    name="code_katas",
    description="Code challenges from CodeWars for the Snow Day.",
    version=0.1,
    author="Julien Wilson",
    author_email="julienawilson@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["last", "string_to_array", "fake_binary",
                "count_positives_sum_negatives", "digitize",
                "binary_list_to_number", "sea_sick", "reverse_and_mirror",
                "flatten_me", "sum_from_string", "multiples"],
    install_requires=[],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov", "tox"]
    }
)
