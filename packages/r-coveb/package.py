# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoveb(RPackage):
	"""Empirical Bayes estimate of block diagonal covariance matrices

	Using bayesian methods to estimate correlation matrices assuming that they can be written and estimated as block diagonal matrices. These block diagonal matrices are determined using shrinkage parameters that values below this parameter to zero.
	"""
	
	bioc = "covEB" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/covEB_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/covEB/covEB_1.28.0.tar.gz"]

	version("1.28.0", md5="5469ab09a3d502902dc4d698abd1cbae")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
