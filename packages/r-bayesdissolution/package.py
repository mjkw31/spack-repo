# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdissolution(RPackage):
	"""Bayesian Models for Dissolution Testing

	Fits Bayesian models to dissolution data sets that can be used for dissolution testing. Currently the package includes the Bayesian models outlined in Pourmohamad et al. (2022) <doi:10.1111/rssc.12535>, but more models may be added over time.
	"""
	
	cran = "BayesDissolution" 

	version("0.1.0", md5="d1b2e6ab1f3673c9b3edbe6ae35346ab")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geor", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
