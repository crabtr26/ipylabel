from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='ipylabel',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="[An ipywidgets dashboard library for converting raw data sources into ML ready datasets.]",
    license="MIT",
    author="Jacob Crabtree",
    author_email='crabtr26@gmail.com',
    url='https://github.com/crabtr26/ipylabel',
    packages=['ipylabel'],
    
    install_requires=requirements,
    keywords='ipylabel',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ]
)
