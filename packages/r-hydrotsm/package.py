# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrotsm(RPackage):
	"""Time Series Management, Analysis and Interpolation for Hydrological
	Modelling.

	S3 functions for management, analysis, interpolation and plotting of time
	series used in hydrology and related environmental sciences. In particular,
	this package is highly oriented to hydrological modelling tasks. The focus
	of this package has been put in providing a collection of tools useful for
	the daily work of hydrologists (although an effort was made to optimise
	each function as much as possible, functionality has had priority over
	speed). Bugs / comments / questions / collaboration of any kind are very
	welcomed, and in particular, datasets that can be included in this package
	for academic purposes."""

	cran = "hydroTSM"

	version("0.7-0", md5="69b491ef36351a9d18dad3b7cbc36843")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-zoo@1.7.2:", type=("build", "run"))
	depends_on("r-xts@0.9.7:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
