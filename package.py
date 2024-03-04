# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class CvmfsSpack(CMakePackage):
    """The CernVM File System provides a scalable, reliable and low-maintenance software distribution service."""

    homepage = "https://cernvm.cern.ch/fs/"
    url = "https://ecsft.cern.ch/dist/cvmfs/cvmfs-2.11.2/cvmfs-2.11.2.tar.gz"

    # list of GitHub accounts to notify when the package is updated.
    # maintainers("ShivamMadlani")

    license("BSD-3-Clause", checked_by="ShivamMadlani")

    version("2.11.2", sha256="a512982cea7c8fab0ecf5b8ecd7c69f33625514bd4d99be3b23060d1826b74e0")

    depends_on("libressl", type="link")
    depends_on("fuse")
    depends_on("libuuid")
    depends_on("zlib")

    def cmake_args(self):
        args = [
            '-DBUILD_SERVER=no',
            '-DBUILD_LIBCVMFS=yes',
            '-DBUILD_CVMFS=no',
            '-DOPENSSL_ROOT_DIR={0}'.format(self.spec['libressl'].prefix),
            '-DOPENSSL_INCLUDE_DIR={0}'.format(join_path(self.spec['libressl'].prefix, 'include')),
            '-DUUID_LIBRARY={0}'.format(self.spec['libuuid'].libs.directories[0]),
            '-DUUID_INCLUDE_DIR={0}'.format(self.spec['libuuid'].headers.directories[0]),
            '-DCMAKE_SHARED_LINKER_FLAGS=-luuid'
            ]
        return args
