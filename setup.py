from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['appcast_view'],
    package_dir={'': 'src'},
    scripts=['nodes/appcast_view.py']
)

setup(**d)
