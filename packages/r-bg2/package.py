# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBg2(RPackage):
	"""Performs Bayesian GWAS analysis for non-Gaussian data using BG2

	This package is built to perform GWAS analysis for non-Gaussian data using BG2. The BG2 method uses penalized quasi-likelihood along with nonlocal priors in a two step manner to identify SNPs in GWAS analysis. The research related to this package was supported in part by National Science Foundation awards DMS 1853549 and DMS 2054173.
	"""
	
	bioc = "BG2" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BG2_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BG2/BG2_1.2.0.tar.gz"]

	version("1.2.0", md5="da6ea59dda3c728bdce70a5b43e4541e", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/BG2_1.2.0.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ga@3.2:", type=("build", "run"))
	depends_on("r-caret@6.0.86:", type=("build", "run"))
	depends_on("r-memoise@1.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.18:", type=("build", "run"))
	depends_on("r-mass@7.3.58.1:", type=("build", "run"))
