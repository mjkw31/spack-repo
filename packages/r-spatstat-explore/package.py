# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatExplore(RPackage):
	"""Exploratory Data Analysis for the 'spatstat' Family.

	Functionality for exploratory data analysis and nonparametric analysis of
	spatial data, mainly spatial point patterns, in the 'spatstat' family of
	packages. (Excludes analysis of spatial data on a linear network, which is
	covered by the separate package 'spatstat.linnet'.) Methods include quadrat
	counts, K-functions and their simulation envelopes, nearest neighbour
	distance and empty space statistics, Fry plots, pair correlation function,
	kernel smoothed intensity, relative risk estimation with cross-validated
	bandwidth selection, mark correlation functions, segregation indices, mark
	dependence diagnostics, and kernel estimates of covariate effects. Formal
	hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte
	Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and
	tests for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov,
	ANOVA) are also supported."""

	cran = "spatstat.explore"

	version("3.2-6", md5="49ee5844d94a714c9bbeb3110ba1ce9e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-data@3.0.1:", type=("build", "run"))
	depends_on("r-spatstat-geom@3.2.8:", type=("build", "run"))
	depends_on("r-spatstat-random@3.2.1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-spatstat-utils@3.0.3:", type=("build", "run"))
	depends_on("r-spatstat-sparse@3.0.1:", type=("build", "run"))
	depends_on("r-goftest@1.2.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
