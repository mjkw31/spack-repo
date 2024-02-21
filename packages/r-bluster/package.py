# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBluster(RPackage):
	"""Clustering Algorithms for Bioconductor.

	Wraps common clustering algorithms in an easily extended S4 framework.
	Backends are implemented for hierarchical, k-means and graph-based
	clustering.  Several utilities are also provided to compare and evaluate
	clustering results."""

	bioc = "bluster"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/bluster_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/bluster/bluster_1.12.0.tar.gz"]

	version("1.12.0", md5="baf91e0700b1f49eb80522be9eb8204d")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
