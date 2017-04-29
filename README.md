# Minimum working example of Cython + OpenMP
Using an example to sum anti diagonals for a stack of square matrices

Make sure your default compiler is GCC. For Mac OSX users, I recommend
installing with Homebrew:

    # Install without-multilib for OpenMP support
    brew install gcc --without-multilib

    # Make sure its the default compiler
    export CC="/usr/local/bin/gcc-x.x"   # <- replace with correct version
    export CXX="/usr/local/bin/g++-x.x"  # <- replace with correct version

To build, run

    python setup.py build_ext --inplace

Then test with

    python test.py



