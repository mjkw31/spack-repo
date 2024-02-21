# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoby(RPackage):
	"""Groupwise Statistics, LSmeans, Linear Estimates, Utilities.

	Utility package containing: 1) Facilities for working with grouped data:
		'do' something to data stratified 'by' some variables. 2) LSmeans
		(least-squares means), general linear estimates. 3) Restrict functions
		to a smaller domain. 4) Miscellaneous other utilities."""

	cran = "doBy"

	version("4.6.20", md5="44c7b48cc7a0d9f57d32010315492372")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
	depends_on("r-pbkrtest@0.4.8.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
