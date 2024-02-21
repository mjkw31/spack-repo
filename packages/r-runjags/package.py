# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunjags(RPackage):
	"""Interface Utilities, Model Templates, Parallel Computing Methods and
	Additional Distributions for MCMC Models in JAGS.

	User-friendly interface utilities for MCMC models via Just Another Gibbs
	Sampler (JAGS), facilitating the use of parallel (or distributed)
	processors for multiple chains, automated control of convergence and sample
	length diagnostics, and evaluation of the performance of a model using
	drop-k validation or against simulated data. Template model specifications
	can be generated using a standard lme4-style formula interface to assist
	users less familiar with the BUGS syntax. A JAGS extension module provides
	additional distributions including the Pareto family of distributions, the
	DuMouchel prior and the half-Cauchy prior."""

	cran = "runjags"

	version("2.2.2-1.1", md5="44ea490b11ff4a9e11b4e15034ec4438")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-lattice@0.20.10:", type=("build", "run"))
	depends_on("r-coda@0.17.1:", type=("build", "run"))
