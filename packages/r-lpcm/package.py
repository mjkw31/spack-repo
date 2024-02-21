# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpcm(RPackage):
	"""Local Principal Curve Methods

	Fitting multivariate data patterns with local principal curves, including tools for data compression (projection) and measuring goodness-of-fit; with some additional functions for mean shift clustering.  See Einbeck, Tutz and Evers (2005) <doi:10.1007/s11222-005-4073-8> and Einbeck (2011) <doi:10.13176/11.288>.
	"""
	
	cran = "LPCM" 

	version("0.47-3", md5="ab5dc2cdf40aee4960cdf515de2d706d")

	depends_on("r@3.5:", type=("build", "run"))
