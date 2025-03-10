# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebook(RPackage):
	"""Re-using Content in Bioconductor Books

	Provides utilities to re-use content across chapters of a Bioconductor book. This is mostly based on functionality developed while writing the OSCA book, but generalized for potential use in other large books with heavy compute. Also contains some functions to assist book deployment.
	"""
	
	bioc = "rebook" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rebook_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rebook/rebook_1.12.0.tar.gz"]

	version("1.12.0", md5="05a8502e7f25563382e9e277b3199339")

	depends_on("r-knitr@1.32:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-codedepends", type=("build", "run"))
	depends_on("r-dir-expiry", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
