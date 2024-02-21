# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastrcs(RPackage):
	"""Fits the FastRCS Robust Multivariable Linear Regression Model

	The FastRCS algorithm of Vakili and Schmitt (2014) for robust fit of the multivariable linear regression model and outliers detection.
	"""
	
	cran = "FastRCS"

	version("0.0.8", md5="4856d791101c97d0d023341656def33e")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
