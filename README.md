# mpi_lsr

mpi4py examples and use mpi4py to implement the parallel least square regression

## reference

- https://github.com/wangshusen/DeepLearning/blob/master/Slides/14_Parallel_1.pdf
- https://mpi4py.readthedocs.io/en/stable/tutorial.html

## Installation

requirement: python3.x , build-essentials(gcc ..)

recommand OS: unix

- build mpi source: https://mpi4py.readthedocs.io/en/stable/appendix.html#building-mpi
    - or download pre-build: https://www.mpich.org/downloads/
    ```
    # sudo user
    sudo ./configure --enable-shared --prefix=/usr/local/mpich
    make
    make install
    ```
    - install distribution version by package management tools: for me(MacOS 13, older version can direct use `brew install mpich`), `brew install --build-from-source mpich` https://formulae.brew.sh/formula/mpich
- pip install mpi4py https://mpi4py.readthedocs.io/en/stable/install.html
- other common packages: numpy

## Build Error

checking whether Fortran 77 and C objects are compatible... no
checking for file... file
checking for linker for Fortran main program... configure: error: Could not determine a way to link a Fortran test program!

Warning: You are using macOS 13.
We do not provide support for this pre-release version.
You will encounter build failures with some formulae.
Please create pull requests instead of asking for help on Homebrew's GitHub,
Twitter or any other official channels. You are responsible for resolving
any issues you experience while you are running this
pre-release version.

Error: texinfo: undefined method `on_monterey' for #<Class:0x00007fab3e924bb8>