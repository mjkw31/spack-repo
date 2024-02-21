# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparedesign(RPackage):
	"""Statistical Functions for the Design of Studies with Composite
Endpoints

	It has been designed to calculate the required sample size in randomized clinical trials with composite endpoints. This package also includes functions to calculate the probability of observing the composite endpoint and the expected effect on the composite endpoint, among others. The methods implemented can be found in  Bofill & Gómez (2019) <doi:10.1002/sim.8092> and Gómez & Lagakos (2013) <doi:10.1002/sim.5547>. 
	"""
	
	cran = "CompAREdesign" 

	version("2.2", md5="93ba6a2f92c0aa5c709ac3814fb7a2fd")

	depends_on("r-copula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
