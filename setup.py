from setuptools import setup, find_packages

setup(
    name='django-waffle',
    version='0.18.0',
    description='A feature flipper for Django.',
    long_description=open('README.rst').read(),
    author='James Socol',
    author_email='me@jamessocol.com',
    url='http://github.com/django-waffle/django-waffle',
    license='BSD',
    packages=find_packages(exclude=['test_app', 'test_settings']),
    include_package_data=True,
    package_data={'': ['README.rst']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        "django<2",
        "importlib-metadata",
    ],
    extras_require={
        "testing": [
            "pytest",
            "pytest-django",
            "mock",
            "django-jinja<2.5",
        ]
    }
)
