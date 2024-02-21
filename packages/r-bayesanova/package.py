# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesanova(RPackage):
	"""Bayesian Inference in the Analysis of Variance via Markov Chain
Monte Carlo in Gaussian Mixture Models

	Provides a Bayesian version of the analysis of variance based on a three-component Gaussian mixture for which a Gibbs sampler produces posterior draws. For details about the Bayesian ANOVA based on Gaussian mixtures, see Kelter (2019) <arXiv:1906.07524>.
	"""
	
	cran = "bayesanova" 

	version("1.5", md5="43a6c2dca8339f59d761f97435d18e54")

	depends_on("r-mcmcpack", type=("build", "run"))
