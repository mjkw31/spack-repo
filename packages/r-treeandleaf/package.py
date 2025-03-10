# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeandleaf(RPackage):
	"""Displaying binary trees with focus on dendrogram leaves

	The TreeAndLeaf package combines unrooted and force-directed graph algorithms in order to layout binary trees, aiming to represent multiple layers of information onto dendrogram leaves.
	"""
	
	bioc = "TreeAndLeaf" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TreeAndLeaf_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TreeAndLeaf/TreeAndLeaf_1.14.0.tar.gz"]

	version("1.14.0", md5="066beb0c7f15d3b6a853bcb68c682f73")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reder@1.40.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
