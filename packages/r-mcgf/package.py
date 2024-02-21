# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcgf(RPackage):
	"""Markov Chain Gaussian Fields Simulation and Parameter Estimation

	Simulating and estimating (regime-switching) Markov chain Gaussian 
    fields with covariance functions of the Gneiting class. It supports 
    parameter estimation by weighted least squares and maximum likelihood 
    methods, and produces Kriging forecasts and intervals (Cressie 1993) 
    <doi:10.1002/9781119115151>.
	"""
	
	homepage = "https://github.com/tianxia-jia/mcgf"
	cran = "mcgf" 

	version("1.0.0", md5="72da2e895fcae96a32877025b14a5958")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
