# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibrar(RPackage):
	"""Automated Parameter Estimation for Complex (Ecological) Models

	Automated parameter estimation for complex (ecological) models in R. 
  This package allows the parameter estimation or calibration of complex models, 
  including stochastic ones. It is a generic tool that can be used for fitting 
  any type of models, especially those with non-differentiable objective functions. 
  It supports multiple phases and constrained optimization. 
  It implements maximum likelihood estimation methods and automated construction 
  of the objective function from simulated model outputs. 
  See <http://roliveros-ramos.github.io/calibrar> for more details.
	"""
	
	homepage = "http://roliveros-ramos.github.io/calibrar"
	cran = "calibrar" 

	version("0.2.0", md5="55196e7e65ef42ce87a91ebdbe2df495")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-cmaes", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
