# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeta(RPackage):
	"""General Package for Meta-Analysis.

	User-friendly general package providing standard methods for meta-analysis
	and supporting Schwarzer, Carpenter, and Rücker
	<doi:10.1007/978-3-319-21416-0>, "Meta-Analysis with R" (2015): - common
	effect and random effects meta-analysis; - several plots (forest, funnel,
	Galbraith / radial, L'Abbe, Baujat, bubble); - three-level meta-analysis
	model; - generalised linear mixed model; - Hartung-Knapp method for random
	effects model; - Kenward-Roger method for random effects model; -
	prediction interval; - statistical tests for funnel plot asymmetry; -
	trim-and-fill method to evaluate bias in meta-analysis; - meta-regression;
	- cumulative meta-analysis and leave-one-out meta-analysis; - import data
	from 'RevMan 5'; - produce forest plot summarising several (subgroup)
	meta-analyses."""

	cran = "meta"

	version("7.0-0", md5="13fa700d2cd0fcc15eb61f391140ce1f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-metadat", type=("build", "run"))
	depends_on("r-metafor@3.0.0:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
