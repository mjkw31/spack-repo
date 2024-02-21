# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsem(RPackage):
	"""Fit Dynamic Structural Equation Models

	Applies dynamic structural equation models to time-series data
	with generic and simplified specification for simultaneous and lagged
	effects. Methods are described in Thorson et al. (In press)
	"Dynamic structural equation models synthesize ecosystem dynamics 
	constrained by ecological mechanisms."  
	"""
	
	homepage = "https://james-thorson-noaa.github.io/dsem/"
	cran = "dsem" 

	version("1.0.2", md5="ccd37cba9276ff21d2648b98e761ab27")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
