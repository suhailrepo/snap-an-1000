from setuptools import setup

setup(
    name='snapshotanalyer3000',
    version='0.1',
    author='Suhail',
    author_email='suhail@local.com',
    description = 'Snapshot analyzer 3000 is a tool to create snapshots of a project or all of the instances.',
    licence="GPLv3+",
    packages=['shotty'],
    url='https://github.com/suhailrepo/snap-an-1000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
