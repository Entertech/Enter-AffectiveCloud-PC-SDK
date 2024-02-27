from setuptools import setup, find_packages


setup(
    name='affectivecloud',
    version='1.2.7',
    description='AffectiveCloud Python SDK',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Natural Language :: Chinese (Simplified)',
        "Development Status :: 4 - Beta",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    url='https://github.com/Entertech/Enter-Affectivecloud-PC-SDK.git',
    author='Lockey',
    author_email='chenyitao@entertech.cn',
    license='Entertech',
    packages=find_packages(
        include=[
            'affectivecloud',
            'affectivecloud.*',
        ],
        exclude=[
            'tests',
            'docs',
            'examples',
            '__pycache__',
            '*.pyc',
            '*.pyo',
        ]
    ),
    include_package_data=False,
    install_requires=[
        'websockets==12.0',
    ],
    dependency_links=[
        'git+https://github.com/Entertech/Enter-Biomodule-BLE-PC-SDK.git@v1.1.4#egg=enterble',
    ],
    zip_safe=False
)
