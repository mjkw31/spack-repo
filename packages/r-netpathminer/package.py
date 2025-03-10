# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetpathminer(RPackage):
	"""NetPathMiner for Biological Network Construction, Path Mining and Visualization

	NetPathMiner is a general framework for network path mining using genome-scale networks. It constructs networks from KGML, SBML and BioPAX files, providing three network representations, metabolic, reaction and gene representations. NetPathMiner finds active paths and applies machine learning methods to summarize found paths for easy interpretation. It also provides static and interactive visualizations of networks and paths to aid manual investigation.
	"""
	
	homepage = "https://github.com/ahmohamed/NetPathMiner"
	bioc = "NetPathMiner"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/NetPathMiner_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/NetPathMiner/NetPathMiner_1.38.0.tar.gz"]

	version("1.38.0", md5="91cc0601961f682fcf1a2bed61eb6438")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
	depends_on("sbml@5.5:", type=("build", "link", "run"))
