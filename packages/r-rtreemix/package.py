# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtreemix(RPackage):
	"""Rtreemix: Mutagenetic trees mixture models.

	Rtreemix is a package that offers an environment for estimating the mutagenetic trees mixture models from cross-sectional data and using them for various predictions. It includes functions for fitting the trees mixture models, likelihood computations, model comparisons, waiting time estimations, stability analysis, etc.
	"""
	
	bioc = "Rtreemix" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Rtreemix_1.64.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Rtreemix/Rtreemix_1.64.0.tar.gz"]

	version("1.64.0", md5="3a9bda84ad8cd784165f1b8ce1a43af7")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
