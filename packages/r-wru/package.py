# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWru(RPackage):
	"""Who are You? Bayesian Prediction of Racial Category Using Surname, First
	Name, Middle Name, and Geolocation

	Predicts individual race/ethnicity using surname, first name, middle name,
	geolocation, and other attributes, such as gender and age. The method
	utilizes Bayes' Rule (with optional measurement error correction) to compute
	the posterior probability of each racial category for any given individual.
	The package implements methods described in Imai and Khanna (2016)
	"Improving Ecological Inference by Predicting Individual Ethnicity from
	Voter Registration Records" Political Analysis <doi:10.1093/pan/mpw001>."""

	homepage = "https://github.com/kosukeimai/wru"
	cran = "wru"

	maintainers("jgaeb")

	version("1.0.1", md5="cfd668eb46d3795b9b88bf952acf7630")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-piggyback@0.1.4:", type=("build", "run"))
	depends_on("r-pl94171", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
