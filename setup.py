from setuptools import setup, find_packages

setup(
    name='niimprint',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'niimprint=niimprint:main',  # Робимо бінарний файл доступним для виконання
        ],
    },
)
