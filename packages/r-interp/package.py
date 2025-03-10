# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterp(RPackage):
	"""Interpolation Methods.

	Bivariate data interpolation on regular and irregular grids, either linear
	or using splines are the main part of this package. It is intended to
	provide FOSS replacement functions for the ACM licensed akima::interp and
	tripack::tri.mesh functions. Linear interpolation is implemented in
	interp::interp(..., method="linear"), this corresponds to the call
	akima::interp(..., linear=TRUE) which is the default setting and covers
	most of akima::interp use cases in depending packages. A re-implementation
	of Akimas irregular grid spline interpolation (akima::interp(...,
	linear=FALSE)) is now also available via interp::interp(...,
	method="akima"). Estimators for partial derivatives are now also available
	in interp::locpoly(), these are a prerequisite for the spline
	interpolation. The basic part is a GPLed triangulation algorithm (sweep
	hull algorithm by David Sinclair) providing the starting point for the
	irregular grid interpolator. As side effect this algorithm is also used to
	provide replacements for almost all functions of the tripack package which
	also suffers from the same ACM license restrictions. All functions are
	designed to be backward compatible with their akima / tripack
	counterparts."""

	cran = "interp"

	version("1.1-6", md5="0a20ffc3aa94cc878b13df35ba09d432")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
