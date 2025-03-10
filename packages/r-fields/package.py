# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFields(RPackage):
	"""Tools for Spatial Data.

	For curve, surface and function fitting with an emphasis; on splines,
	spatial data, geostatistics,  and spatial statistics. The major methods;
	include cubic, and thin plate splines, Kriging, and compactly supported;
	covariance functions for large data sets. The splines and Kriging methods
	are; supported by functions that can determine the smoothing parameter;
	(nugget and sill variance) and other covariance function parameters by
	cross; validation and also by restricted maximum likelihood. For Kriging;
	there is an easy to use function that also estimates the correlation; scale
	(range parameter).  A major feature is that any covariance function;
	implemented in R and following a simple format can be used for; spatial
	prediction. There are also many useful functions for plotting; and working
	with spatial data as images. This package also contains; an implementation
	of sparse matrix methods for large spatial data; sets and currently
	requires the sparse matrix (spam) package. Use; help(fields) to get started
	and for an overview.  The fields source; code is deliberately commented and
	provides useful explanations of; numerical details as a companion to the
	manual pages. The commented; source code can be viewed by expanding the
	source code version; and looking in the R subdirectory. The reference for
	fields can be generated; by the citation function in R and has DOI
	<doi:10.5065/D6W957CT>. Development; of this package was supported in part
	by the National Science Foundation  Grant; 1417857,  the National Center
	for Atmospheric Research, and Colorado School of Mines.; See the Fields
	URL; for a vignette on using this package and some background on spatial
	statistics."""

	cran = "fields"

	version("15.2", md5="65adac2c1597e57e7e27fb88df6a6641")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
