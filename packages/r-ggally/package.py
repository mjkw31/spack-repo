# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgally(RPackage):
	"""Extension to 'ggplot2'.

	The R package 'ggplot2' is a plotting system based on the grammar of
	graphics. 'GGally' extends 'ggplot2' by adding several functions to reduce
	the complexity of combining geometric objects with transformed data. Some
	of these functions include a pairwise plot matrix, a two group pairwise
	plot matrix, a parallel coordinates plot, a survival plot, and several
	functions to plot networks."""

	cran = "GGally"

	version("2.2.1", md5="9acff4b4e2fd3197ac98fada1266434a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-ggstats", type=("build", "run"))
	depends_on("r-gtable@0.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("openssl", type=("build", "link", "run"))
