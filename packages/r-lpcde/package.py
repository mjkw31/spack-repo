# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpcde(RPackage):
	"""Boundary Adaptive Local Polynomial Conditional Density Estimator

	Tools for estimation and inference of conditional densities, derivatives and functions. This is the companion software for Cattaneo, Chandak, Jansson and Ma (2022).
	"""
	
	cran = "lpcde"

	version("0.1.1", md5="ccce545aace19b82fd1a2aa81163564a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
