# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplyagree(RPackage):
	"""Flexible and Robust Agreement and Reliability Analyses

	Reliability and agreement analyses often have limited software support. Therefore, this package was created to make agreement and reliability analyses easier for the average researcher. The functions within this package include simple tests of agreement, agreement analysis for nested and replicate data, and provide robust analyses of reliability. In addition, this package contains a set of functions to help when planning studies looking to assess measurement agreement. For robust analyses of agreement, limits of agreement through a bootstrap method can also be calculated.
	"""
	
	homepage = "https://aaroncaldwell.us/SimplyAgree/"
	cran = "SimplyAgree" 

	version("0.1.2", md5="1a49cee55c4d14a513502a21c8c6ff3e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jmvcore", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
