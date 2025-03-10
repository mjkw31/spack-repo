# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChicago(RPackage):
	"""CHiCAGO: Capture Hi-C Analysis of Genomic Organization

	A pipeline for analysing Capture Hi-C data.
	"""
	
	bioc = "Chicago" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Chicago_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Chicago/Chicago_1.30.0.tar.gz"]

	version("1.30.0", md5="854dccdecc3b0fc55c9146908bdeec27")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-delaporte", type=("build", "run"))
