# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShrinktvp(RPackage):
	"""Efficient Bayesian Inference for Time-Varying Parameter Models
with Shrinkage

	Efficient Markov chain Monte Carlo (MCMC) algorithms for fully Bayesian estimation of time-varying parameter models with shrinkage priors. Details on the algorithms used are provided in Bitto and Frühwirth-Schnatter (2019) <doi:10.1016/j.jeconom.2018.11.006> and  
  Cadonna et al. (2020) <doi:10.3390/econometrics8020020>. For details on the package, please see Knaus et al. (2021) <doi:10.18637/jss.v100.i13>.
	"""
	
	cran = "shrinkTVP" 

	version("2.1.1", md5="40145a4f765710313c5a345953616a5a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-stochvol", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
