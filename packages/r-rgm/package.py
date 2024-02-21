# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgm(RPackage):
	"""Advanced Inference with Random Graphical Models

	Implements state-of-the-art Random Graphical Models (RGMs) for multivariate data analysis across multiple environments, offering tools for exploring network interactions and structural relationships. Capabilities include joint inference across environments, integration of external covariates, and a Bayesian framework for uncertainty quantification. Applicable in various fields, including microbiome analysis. Methods based on Vinciotti, V., Wit, E., & Richter, F. (2023). "Random Graphical Model of Microbiome Interactions in Related Environments." <arXiv:2304.01956>.
	"""
	
	cran = "rgm" 

	version("1.0.1", md5="0e459af185a457b024709ec46748811f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-bdgraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
