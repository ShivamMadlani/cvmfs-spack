# cvmfs-spack
Spack recipe for building CVMFS

## Building CVMFS without spack
```bash
cd <source directory>
mkdir build && cd build
cmake ../
make
sudo make install
```

## Building with spack
```bash
spack install cvmfs-spack
```
Spack will automatically follow the following steps for this project:
```bash
mkdir spack-build
cd spack-build
cmake .. 
make
make test  # optional
make install
```

## Getting package info
Run the below command to get the package details
```bash
spack info cvmfs-spack
```

## CVMFS dependencies
1. fuse
2. libressl
3. zlib
4. libuuid