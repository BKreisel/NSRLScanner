try:
    from setuptools import setup
except ImportError:
    print("setuptools module not found")

config = {
    'description': 'NIST NSLR Scanner for OS X',
    'author': 'Brandon Kreisel',
    'url': 'https://www.github.com/bkreisel/MacNSRL',
    'download_url': 'https://www.github.com/bkreisel/MacNSRL',
    'author_email': 'kreiselb@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['macnsrl'],
    'scripts': [],
    'entry_points': {
        'console_scripts': [
            'macnsrl = macnsrl.cli:main'
        ]
    },
    'name': 'MacNSRL'
}

setup(**config)
