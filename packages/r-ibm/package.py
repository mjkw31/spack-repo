# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbm(RPackage):
	"""Individual Based Models in R

	Implementation of some (simple) Individual Based Models and methods
  to create new ones, particularly for population dynamics models (reproduction, 
  mortality and movement). The basic operations for the simulations are 
  implemented in Rcpp for speed.
	"""
	
	homepage = "http://roliveros-ramos.github.io/ibm"
	cran = "ibm" 

	version("0.1.0", md5="bf1580f3788c2397d8e88e71ede2bdfb")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
