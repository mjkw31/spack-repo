# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmc(RPackage):
	"""Markov Chain Monte Carlo.

	Simulates continuous distributions of random vectors using Markov chain
	Monte Carlo (MCMC). Users specify the distribution by an R function that
	evaluates the log unnormalized density. Algorithms are random walk
	Metropolis algorithm (function metrop), simulated tempering (function
	temper), and morphometric random walk Metropolis (Johnson and Geyer, 2012,
	<doi:10.1214/12-AOS1048>, function morph.metrop), which achieves geometric
	ergodicity by change of variable."""

	cran = "mcmc"

	version("0.9-8", md5="429599a7f24105629c41dd7c9f36b992")

	depends_on("r@3.6:", type=("build", "run"))
