# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankprod(RPackage):
	"""Rank Product method for identifying differentially expressed genes with application in meta-analysis

	Non-parametric method for identifying differentially expressed (up- or down- regulated) genes based on the estimated percentage of false predictions (pfp). The method can combine data sets from different origins (meta-analysis) to increase the power of the identification.
	"""
	
	bioc = "RankProd" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RankProd_3.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RankProd/RankProd_3.28.0.tar.gz"]

	version("3.28.0", md5="39f3eba64601984ad265d91f3a150180")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
