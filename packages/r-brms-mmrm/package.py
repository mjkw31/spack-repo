# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrmsMmrm(RPackage):
	"""Bayesian MMRMs using 'brms'

	The mixed model for repeated measures (MMRM) is a
  popular model for longitudinal clinical trial data with
  continuous endpoints, and 'brms' is a powerful and versatile
  package for fitting Bayesian regression models.
  The 'brms.mmrm' R package leverages 'brms' to run MMRMs, and
  it supports a simplified interfaced to reduce difficulty
  and align with the best practices of the life sciences.
  References: Bürkner (2017) <doi:10.18637/jss.v080.i01>,
  Mallinckrodt (2008) <doi:10.1177/009286150804200402>.
	"""
	
	homepage = "https://openpharma.github.io/brms.mmrm/"
	cran = "brms.mmrm" 

	version("0.0.2", md5="4d9ed7ee379387b5b311d3c237e1c78d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emmeans@1.8.7:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-trialr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
