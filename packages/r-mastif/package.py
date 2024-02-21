# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMastif(RPackage):
	"""Mast Inference and Forecasting

	Analyzes production and dispersal of seeds dispersed from trees and recovered in seed traps.  Motivated by long-term inventory plots where seed collections are used to infer seed production by each individual plant. 
	"""
	
	cran = "mastif" 

	version("2.1", md5="247cf313cac7bbe44e058faa9d086a89")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-repmis", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
