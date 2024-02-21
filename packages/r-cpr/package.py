# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpr(RPackage):
	"""Control Polygon Reduction

	Implementation of the Control Polygon Reduction and Control Net
    Reduction methods for finding parsimonious B-spline regression models.
	"""
	
	homepage = "https://github.com/dewittpe/cpr/"
	cran = "cpr" 

	version("0.3.0", md5="384d2c491e850aabbc3ec8146444078e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rcpp@1.0.11:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
