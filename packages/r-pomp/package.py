# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPomp(RPackage):
	"""Statistical Inference for Partially Observed Markov Processes

	Tools for data analysis with partially observed Markov process (POMP) models (also known as stochastic dynamical systems, hidden Markov models, and nonlinear, non-Gaussian, state-space models).  The package provides facilities for implementing POMP models, simulating them, and fitting them to time series data by a variety of frequentist and Bayesian methods.  It is also a versatile platform for implementation of inference methods for general POMP models.
	"""
	
	homepage = "https://kingaa.github.io/pomp/"
	cran = "pomp"

	version("5.5", md5="0927b62645deef86ba8d92a6b84ba4bf")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
