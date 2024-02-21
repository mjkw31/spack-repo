# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcompanion(RPackage):
	"""Functions to Support Extension Education Program Evaluation

	Functions and datasets to support Summary and Analysis of
             Extension Program Evaluation in R, and An R
             Companion for the Handbook of Biological Statistics. 
             Vignettes are available at <https://rcompanion.org>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=rcompanion"
	cran = "rcompanion" 

	version("2.4.34", md5="05a0c4fd98483fd986e4f5b4543a8de0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-boot@1.3.28:", type=("build", "run"))
	depends_on("r-desctools@0.99.43:", type=("build", "run"))
	depends_on("r-multcompview@0.1.8:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-coin@1.4.2:", type=("build", "run"))
	depends_on("r-lmtest@0.9.38:", type=("build", "run"))
	depends_on("r-nortest@1.0.4:", type=("build", "run"))
