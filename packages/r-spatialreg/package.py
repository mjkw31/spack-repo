# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialreg(RPackage):
	"""Spatial Regression Analysis.

	A collection of all the estimation functions for spatial cross-sectional
	models (on lattice/areal data using spatial weights matrices) contained up
	to now in 'spdep', 'sphet' and 'spse'. These model fitting functions
	include maximum likelihood methods for cross-sectional models proposed by
	'Cliff' and 'Ord' (1973, ISBN:0850860369) and (1981, ISBN:0850860814),
	fitting methods initially described by 'Ord' (1975)
	<doi:10.1080/01621459.1975.10480272>. The models are further described by
	'Anselin' (1988) <doi:10.1007/978-94-015-7799-1>. Spatial two stage least
	squares and spatial general method of moment models initially proposed by
	'Kelejian' and 'Prucha' (1998) <doi:10.1023/A:1007707430416> and (1999)
	<doi:10.1111/1468-2354.00027> are provided. Impact methods and MCMC fitting
	methods proposed by 'LeSage' and 'Pace' (2009) <doi:10.1201/9781420064254>
	are implemented for the family of cross-sectional spatial regression
	models. Methods for fitting the log determinant term in maximum likelihood
	and MCMC fitting are compared by 'Bivand et al.' (2013)
	<doi:10.1111/gean.12008>, and model fitting methods by 'Bivand' and 'Piras'
	(2015) <doi:10.18637/jss.v063.i18>; both of these articles include
	extensive lists of references. 'spatialreg' >= 1.1-* correspond to 'spdep'
	>= 1.1-1, in which the model fitting functions are deprecated and pass
	through to 'spatialreg', but will mask those in 'spatialreg'. From versions
	1.2-*, the functions will be made defunct in 'spdep'."""

	cran = "spatialreg"

	version("1.3-2", md5="c832754d3d9a3bd5315204b2e6052683")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spdep@1.3.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-learnbayes", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
