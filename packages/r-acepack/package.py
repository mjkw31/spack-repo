# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcepack(RPackage):
	"""ACE and AVAS for Selecting Multiple Regression Transformations.

	Two nonparametric methods for multiple regression transform selection are
	provided. The first, Alternative Conditional Expectations (ACE), is an
	algorithm to find the fixed point of maximal correlation, i.e. it finds a
	set of transformed response variables that maximizes R^2 using smoothing
	functions [see Breiman, L., and J.H. Friedman. 1985. "Estimating Optimal
	Transformations for Multiple Regression and Correlation". Journal of the
	American Statistical Association. 80:580-598.
	<doi:10.1080/01621459.1985.10478157>]. Also included is the Additivity
	Variance Stabilization (AVAS) method which works better than ACE when
	correlation is low [see Tibshirani, R.. 1986. "Estimating Transformations
	for Regression via Additivity and Variance Stabilization". Journal of the
	American Statistical Association. 83:394-405.
	<doi:10.1080/01621459.1988.10478610>]. A good introduction to these two
	methods is in chapter 16 of Frank Harrel's "Regression Modeling Strategies"
	in the Springer Series in Statistics."""

	cran = "acepack"

	version("1.4.2", md5="c1c2bee3f296f3251b7595514b2ef239")

