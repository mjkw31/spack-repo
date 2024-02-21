# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMendelianrandomization(RPackage):
	"""Mendelian Randomization Package.

	Encodes several methods for performing Mendelian randomization analyses
	with summarized data. Summarized data on genetic associations with the
	exposure and with the outcome can be obtained from large consortia. These
	data can be used for obtaining causal estimates using instrumental variable
	methods."""

	cran = "MendelianRandomization"

	version("0.9.0", md5="243c59b46fd305672205b094a9ae0b90")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-plotly@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-robustbase@0.92.6:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-iterpc@0.3:", type=("build", "run"))
	depends_on("r-quantreg@5.1:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
