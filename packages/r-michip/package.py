# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMichip(RPackage):
	"""MiChip Parsing and Summarizing Functions

	This package takes the MiChip miRNA microarray .grp scanner output files and parses these out, providing summary and plotting functions to analyse MiChip hybridizations. A set of hybridizations is packaged into an ExpressionSet allowing it to be used by other BioConductor packages.
	"""
	
	bioc = "MiChip" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MiChip_1.56.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MiChip/MiChip_1.56.0.tar.gz"]

	version("1.56.0", md5="28daafdf6588314a9fad7a75b1671c10")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
