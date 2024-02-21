# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasilisk(RPackage):
	"""Freezing Python Dependencies Inside Bioconductor Packages.

	Installs a self-contained conda instance that is managed by the
	R/Bioconductor installation machinery. This aims to provide a consistent
	Python environment that can be used reliably by Bioconductor packages.
	Functions are also provided to enable smooth interoperability of multiple
	Python environments in a single R session."""

	bioc = "basilisk"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/basilisk_1.14.3.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/basilisk/basilisk_1.14.3.tar.gz"]

	version("1.14.3", md5="0ae86374eec47c3b808cf10947d2695b")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-dir-expiry", type=("build", "run"))
	depends_on("r-basilisk-utils@1.14.1:", type=("build", "run"))
