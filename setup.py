from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    'numpy',
    'pysolar'
]


setup(name='PARpy',
    version=version,
    description="Processing tool for PAR data of Satlantic Radiometers",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Topic :: Scientific/Engineering',
          ],
    keywords='PAR satlantic oceanography light photosynthetcally',
    author='Arnaldo Russo',
    author_email='arnaldorusso@gmail.com',
    url='ciclotux.blogspot.com',
    license='PSF',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    #entry_points={
    #    'console_scripts':
    #        ['PAR_model=par_model:main']
    }
)
