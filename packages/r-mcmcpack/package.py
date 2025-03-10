# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcpack(RPackage):
	"""Markov Chain Monte Carlo (MCMC) Package.

	Contains functions to perform Bayesian inference using posterior simulation
	for a number of statistical models. Most simulation is done in compiled C++
	written in the Scythe Statistical Library Version 1.0.3. All models return
	'coda' mcmc objects that can then be summarized using the 'coda' package.
	Some useful utility functions such as density functions, pseudo-random
	number generators for statistical distributions, a general purpose
	Metropolis sampling algorithm, and tools for visualization are provided."""

	cran = "MCMCpack"

	version("1.7-0", md5="b17248f41c8121305c9121b770f44c94")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-coda@0.11.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mcmc", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("gcc@4.0:", type=("build", "link", "run"))

	conflicts("%gcc@:3")
