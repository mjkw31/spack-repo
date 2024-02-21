# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmdcev(RPackage):
	"""Kuhn-Tucker and Multiple Discrete-Continuous Extreme Value
Models

	Estimates and simulates Kuhn-Tucker demand models with individual heterogeneity. The package implements the multiple-discrete continuous extreme value (MDCEV) model and the Kuhn-Tucker specification common in the environmental economics literature on recreation demand. Latent class and random parameters specifications can be implemented and the models are fit using maximum likelihood estimation or Bayesian estimation. All models are implemented in Stan, which is a C++ package for performing full Bayesian inference (see Stan Development Team, 2019) <https://mc-stan.org/>. The package also implements demand forecasting (Pinjari and Bhat (2011) <https://repositories.lib.utexas.edu/handle/2152/23880>) and welfare calculation (Lloyd-Smith (2018) <doi:10.1016/j.jocm.2017.12.002>) for policy simulation.
	"""
	
	homepage = "https://github.com/plloydsmith/rmdcev"
	cran = "rmdcev"

	version("1.2.5", md5="1e63743b72c257d184cfba8a12adb9a6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rstan@2.21:", type=("build", "run"))
	depends_on("r-rstantools@2.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-bh@1.72:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.21:", type=("build", "run"))
