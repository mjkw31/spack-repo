# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvhar(RPackage):
	"""Bayesian Vector Heterogeneous Autoregressive Modeling

	Tools to research Bayesian Vector heterogeneous autoregressive (VHAR) model,
    referring to Kim & Baek (2023) (<doi:10.1080/00949655.2023.2281644>).
    'bvhar' can model Vector Autoregressive (VAR), VHAR, Bayesian VAR (BVAR), and Bayesian VHAR (BVHAR) models.
	"""
	
	homepage = "https://ygeunkim.github.io/package/bvhar/"
	cran = "bvhar" 

	version("1.2.0", md5="71a2b6f9c7489fac496a9db51c02817d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
