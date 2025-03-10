# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinystan(RPackage):
	"""Interactive Visual and Numerical Diagnostics and Posterior Analysis for
	Bayesian Models.

	A graphical user interface for interactive Markov chain Monte Carlo (MCMC)
	diagnostics and plots and tables helpful for analyzing a posterior sample.
	The interface is powered by the 'Shiny' web application framework from
	'RStudio' and works with the output of MCMC programs written in any
	programming language (and has extended functionality for 'Stan' models fit
	using the 'rstan' and 'rstanarm' packages)."""

	cran = "shinystan"

	version("2.6.0", md5="23bbac40f95a658610d51e891aba6edd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-shiny@1.0.3:", type=("build", "run"))
	depends_on("r-bayesplot@1.5:", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-dygraphs@1.1.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.1.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-markdown@0.7.4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstan@2.17.1:", type=("build", "run"))
	depends_on("r-shinyjs@0.6:", type=("build", "run"))
	depends_on("r-shinythemes@1.0.1:", type=("build", "run"))
	depends_on("r-threejs@0.2.1:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-xts@0.9.7:", type=("build", "run"))
