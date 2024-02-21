# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRumidas(RPackage):
	"""Univariate GARCH-MIDAS, Double-Asymmetric GARCH-MIDAS and
MEM-MIDAS

	Adds the MIxing-Data Sampling (MIDAS, Ghysels et al. (2007) <doi:10.1080/07474930600972467>) components to a variety of GARCH and MEM (Engle (2002) <doi:10.1002/jae.683>) models, with the aim of predicting the volatility with additional low-frequency (that is, MIDAS) terms. The estimation takes place through simple functions, which provide in-sample and (if present) and out-of-sample evaluations. 'rumidas' also offers a summary tool, which synthesizes the main information of the estimated model. There is also the possibility of generating one-step-ahead and multi-step-ahead forecasts. 
	"""
	
	cran = "rumidas" 

	version("0.1.1", md5="8d9fb595722adaf485930035056702c8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-maxlik@1.3.8:", type=("build", "run"))
	depends_on("r-highfrequency@0.6.5:", type=("build", "run"))
	depends_on("r-roll@1.1.4:", type=("build", "run"))
	depends_on("r-xts@0.12:", type=("build", "run"))
	depends_on("r-tseries@0.10.47:", type=("build", "run"))
	depends_on("r-rdpack@1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-zoo@1.8.8:", type=("build", "run"))
