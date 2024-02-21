# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsv(RPackage):
	"""Stochastic Volatility Models with or without Leverage

	The efficient Markov chain Monte Carlo estimation of stochastic volatility models with and without leverage (asymmetric and symmetric stochastic volatility models). Further, it computes the logarithm of the likelihood given parameters using particle filters.
	"""
	
	homepage = "https://sites.google.com/view/omori-stat/english/software/asv-r"
	cran = "ASV" 

	version("1.1.2", md5="a2a8077c2dd8b47d3855f622423c70fc")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-freqdom", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
