# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneticsped(RPackage):
	"""Pedigree and genetic relationship functions

	Classes and methods for handling pedigree data. It also includes functions to calculate genetic relationship measures as relationship and inbreeding coefficients and other utilities. Note that package is not yet stable. Use it with care!
	"""
	
	homepage = "http://rgenetics.org"
	bioc = "GeneticsPed" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GeneticsPed_1.64.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GeneticsPed/GeneticsPed_1.64.0.tar.gz"]

	version("1.64.0", md5="7d2a79c363e79459dd3edf3b4571f313")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-genetics", type=("build", "run"))
