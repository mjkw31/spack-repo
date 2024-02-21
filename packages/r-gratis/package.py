# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGratis(RPackage):
	"""Generating Time Series with Diverse and Controllable
Characteristics

	
  Generates synthetic time series based on various univariate time series models
  including MAR and ARIMA processes. Kang, Y., Hyndman, R.J., Li, F.(2020) <doi:10.1002/sam.11461>.
	"""
	
	homepage = "https://github.com/ykang/gratis"
	cran = "gratis" 

	version("1.0.5", md5="222e06d57898881981df553716d6e9a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-forecast@8.16:", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tsfeatures", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
