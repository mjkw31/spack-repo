# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeometries(RPackage):
	"""Convert Between R Objects and Geometric Structures.

	Geometry shapes in 'R' are typically represented by matrices (points,
	lines), with more complex shapes being lists of matrices (polygons).
	'Geometries' will convert various 'R' objects into these shapes. Conversion
	functions are available at both the 'R' level, and through 'Rcpp'."""

	cran = "geometries"

	version("0.2.4", md5="2ec0da94482c6d0159dc6b159ed344e6")

	depends_on("r-rcpp", type=("build", "run"))
