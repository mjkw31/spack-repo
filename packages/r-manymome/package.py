# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManymome(RPackage):
	"""Mediation, Moderation and Moderated-Mediation After Model
Fitting

	Computes indirect effects, conditional effects, and conditional
  indirect effects in a structural equation model or path model after model
  fitting, with no need to define any user parameters or label any paths in
  the model syntax, using the approach presented in Cheung and Cheung
  (2023) <doi:10.3758/s13428-023-02224-z>. Can also form bootstrap
  confidence intervals by doing bootstrapping only once and reusing the
  bootstrap estimates in all subsequent computations. Supports bootstrap
  confidence intervals for standardized (partially or completely) indirect
  effects, conditional effects, and conditional indirect effects as described
  in Cheung (2009) <doi:10.3758/BRM.41.2.425> and Cheung, Cheung, Lau, Hui,
  and Vong (2022) <doi:10.1037/hea0001188>. Model fitting can be done by
  structural equation modeling using lavaan() or regression using lm().
	"""
	
	homepage = "https://sfcheung.github.io/manymome/"
	cran = "manymome" 

	version("0.1.13", md5="b0ef69ef2197de270adb43ae4e46b21f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
