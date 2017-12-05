from setuptools import setup, find_packages


setup(
    name="Finger balabolka",
    version='1.0.14',
    description="A project of flood chat.",
    long_description="A flood chat-client project on ptyhon 3 and PyQt5",
    author="Artem Sukharenko",
    author_email="truecyxapic@yandex.ru",
    url="https://github.com/Cyxapic/fb_client",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Flood chat for lern',
    packages=find_packages('fb_client'),
    package_dir={'':'fb_client'},
    package_data={
        '': ['*.jpg','*.png', '*.gif'],
        'ui': ['img/*.jpg', 'img/*.png', 'img/*.gif'],
    },
    install_requires=[
        "Pillow==4.3.0",
        "PyQt5==5.9",
        "SQLAlchemy==1.1.14",
    ],
    extras_require={
        'dev': ['flake8==3.4.1',],
        'test': ["pytest==3.2.2",
                 "pytest-cov==2.5.1",
                 "pytest-sugar==0.9.0",
                 "PyYAML==3.12",],
    },
    entry_points={
        'gui_scripts': [
            'finger_balabolka = fb_client.main:main',
        ]
    },
)