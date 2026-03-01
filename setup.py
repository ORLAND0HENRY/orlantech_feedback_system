from setuptools import setup, find_packages

setup(
    name='orlantech-nexus-orlantech_feedback',
    version='1.0.0',
    description='A standalone, AJAX-powered universal orlantech_feedback system for Django projects.',
    author='Orlantech Innovations',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=4.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)