# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetboost(RPackage):
	"""Network Analysis Supported by Boosting

	Boosting supported network analysis for high-dimensional omics applications. This package comes bundled with the MC-UPGMA clustering package by Yaniv Loewenstein.
	"""
	
	homepage = "https://bioconductor.org/packages/release/bioc/html/netboost.html"
	bioc = "netboost"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/netboost_2.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/netboost/netboost_2.10.0.tar.gz"]

	version("2.10.0", md5="d21f645a3fe85c35ff9b9127bce1fbca")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
	depends_on("gzip", type=("build", "link", "run"))
