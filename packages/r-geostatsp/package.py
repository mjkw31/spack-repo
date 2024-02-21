# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeostatsp(RPackage):
	"""Geostatistical Modelling with Likelihood and Bayes

	Geostatistical modelling facilities using 'SpatRaster' and 'SpatVector'
    objects are provided. Non-Gaussian models are fit using 'INLA', and Gaussian
    geostatistical models use Maximum Likelihood Estimation.  For details see Brown (2015) <doi:10.18637/jss.v063.i12>. The 'RandomFields' package is available at <https://www.wim.uni-mannheim.de/schlather/publications/software>.
	"""
	
	cran = "geostatsp" 

	version("2.0.3", md5="7ea0ef16c1c6ad0010c3831e84daa311")

	depends_on("r-matrix@1.6.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
