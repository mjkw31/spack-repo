# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefund(RPackage):
	"""Regression with Functional Data

	Methods for regression for functional
    data, including function-on-scalar, scalar-on-function, and
    function-on-function regression. Some of the functions are applicable to
    image data.
	"""
	
	cran = "refund" 

	version("0.1-34", md5="d157e591b6a25fbf278cbd56c2d3bc9e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mgcv@1.9:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rlrsim", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pbs", type=("build", "run"))
