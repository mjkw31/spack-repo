# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatLinnet(RPackage):
	"""Linear Networks Functionality of the 'spatstat' Family.

	Defines types of spatial data on a linear network and provides
	functionality for geometrical operations, data analysis and modelling of
	data on a linear network, in the 'spatstat' family of packages. Contains
	definitions and support for linear networks, including creation of
	networks, geometrical measurements, topological connectivity, geometrical
	operations such as inserting and deleting vertices, intersecting a network
	with another object, and interactive editing of networks. Data types
	defined on a network include point patterns, pixel images, functions, and
	tessellations. Exploratory methods include kernel estimation of intensity
	on a network, K-functions and pair correlation functions on a network,
	simulation envelopes, nearest neighbour distance and empty space distance,
	relative risk estimation with cross-validated bandwidth selection. Formal
	hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte
	Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and
	tests for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov,
	ANOVA) are also supported. Parametric models can be fitted to point pattern
	data using the function lppm() similar to glm(). Only Poisson models are
	implemented so far. Models may involve dependence on covariates and
	dependence on marks. Models are fitted by maximum likelihood. Fitted point
	process models can be simulated, automatically. Formal hypothesis tests of
	a fitted model are supported (likelihood ratio test, analysis of deviance,
	Monte Carlo tests) along with basic tools for model selection (stepwise(),
	AIC()) and variable selection (sdr). Tools for validating the fitted model
	include simulation envelopes, residuals, residual plots and Q-Q plots,
	leverage and influence diagnostics, partial residuals, and added variable
	plots. Random point patterns on a network can be generated using a variety
	of models."""

	cran = "spatstat.linnet"

	version("3.1-4", md5="eb5ec2232e1c48646dd4bd6ca64f4e68")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-data@3:", type=("build", "run"))
	depends_on("r-spatstat-geom@3.2.7:", type=("build", "run"))
	depends_on("r-spatstat-random@3.2.1:", type=("build", "run"))
	depends_on("r-spatstat-explore@3.2.5:", type=("build", "run"))
	depends_on("r-spatstat-model@3.2.9:", type=("build", "run"))
	depends_on("r-spatstat-utils@3.0.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spatstat-sparse@3:", type=("build", "run"))
