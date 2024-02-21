# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigsimr(RPackage):
	"""Fast Generation of High-Dimensional Random Vectors

	Simulate multivariate data with arbitrary marginal distributions.
  'bigsimr' is an package for simulating high-dimensional multivariate data with a target correlation and arbitrary marginal distributions via Gaussian copula. 
  It utilizes a Julia package named 'Bigsimr.jl' for its core routines.
	"""
	
	homepage = "https://github.com/SchisslerGroup/r-bigsimr"
	cran = "bigsimr"

	version("0.11.2", md5="874fc5d98ace0a970c993aa3a58554a1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-juliacall", type=("build", "run"))
	depends_on("julia@1.5:", type=("build", "link", "run"))
