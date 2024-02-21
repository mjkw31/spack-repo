# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManynet(RPackage):
	"""Many Ways to Make, Modify, Mark, and Map Myriad Networks

	A set of tools for making, modifying, marking, and mapping many different types of networks.
   All functions operate with matrices, edge lists, and 'igraph', 'network', and 'tidygraph' objects,
   and on one-mode, two-mode (bipartite), and sometimes three-mode networks.
   The package includes functions for importing and exporting, creating and generating networks,
   modifying networks and node and tie attributes,
   and describing and visualizing networks with sensible defaults.
	"""
	
	homepage = "https://stocnet.github.io/manynet/"
	cran = "manynet" 

	version("0.4.1", md5="c505c8cf9d106a6d6ff92b3e6f9024b3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph@1.6:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
