import setuptools

setuptools.setup(
    name='zpp',
    version='0.0.0',
    author='Andrew Henry',
    author_email='andrewmichaelhenry@gmail.com',
    packages=['zpp'],
    entry_points={
        'console_scripts': ['zpp=zpp.zpp:main']
        }
)
