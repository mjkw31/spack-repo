# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyfaidx(PythonPackage):
    """pyfaidx: efficient pythonic random access to fasta subsequences"""

    pypi = "pyfaidx/pyfaidx-0.5.5.2.tar.gz"

    version("0.8.1.1", sha256="6f0482352619f2cc56003ca22321bdb0d0764b656795bc1e4062b1fa9b08686b")
    version("0.5.5.2", sha256="9ac22bdc7b9c5d995d32eb9dc278af9ba970481636ec75c0d687d38c26446caa")

    depends_on("py-setuptools@0.7:", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
