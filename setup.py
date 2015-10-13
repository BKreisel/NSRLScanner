try:
    from setuptools import setup
except ImportError:
    print("setuptools module not found")

config = {
    'description': 'NIST NSLR Scanner',
    'author': 'Brandon Kreisel',
    'url': 'https://www.github.com/bkreisel/NSRLScanner',
    'download_url': 'https://www.github.com/bkreisel/NSRLScanner',
    'author_email': 'kreiselb@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['nsrlscanner'],
    'scripts': [],
    'entry_points': {
        'console_scripts': [
            'nsrlscanner = nsrlscanner.cli:main'
        ]
    },
    'name': 'NSRLScanner'
}

setup(**config)
