# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REulerr(RPackage):
	"""Area-Proportional Euler and Venn Diagrams with Ellipses

	Generate area-proportional Euler diagrams
	using numerical optimization. An Euler diagram is a generalization of a Venn
	diagram, relaxing the criterion that all interactions need to be
	represented. Diagrams may be fit with ellipses and circles via
	a wide range of inputs and can be visualized in numerous ways.
	"""
	
	homepage = "https://github.com/jolars/eulerr"
	cran = "eulerr"

	version("7.0.0", md5="221f2cac8fd23eb8b7402b2ead122a09")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-polyclip", type=("build", "run"))
	depends_on("r-polylabelr", type=("build", "run"))
	depends_on("r-rcpp@0.12.12:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
