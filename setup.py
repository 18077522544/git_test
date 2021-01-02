import setuptools

setuptools.setup(
    name='pypi-test-example',
    version='0.1',
    description='django install by pypi',
    author="phl",
    author_email="author@example.com",
    url="https://github.com/pypa/sampleproject",
    license='MIT',
    packages=setuptools.find_packages('pypi-test-example'),
    package_dir={'': 'pypi-test-example'},
    # package_data={'':[]},#需要打包的数据
    install_requires=[
        'django~=3.1.4'
    ],
    extras_requires={
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'pypi-test-example/manage.py',
    ],
    entry_points={
        'console_scripts': [
            'pypy_test_manage=manage:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 -Alpha',
        'Topic :: Software Development :: Libraies',
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
