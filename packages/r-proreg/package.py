# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProreg(RPackage):
	"""Patient Reported Outcomes Regression Analysis

	Offers a variety of tools, such as specific plots and regression model approaches, for analyzing different patient reported questionnaires. Specially, mixed-effects models based on the beta-binomial distribution are implemented to deal with binomial data with over-dispersion  (see Najera-Zuloaga J., Lee D.-J. and Arostegui I. (2018) <doi:10.1177/0962280217690413>).
	"""
	
	cran = "PROreg" 

	version("1.2", md5="4b909bbfc279b6a8b844b07007c94e33")

	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
