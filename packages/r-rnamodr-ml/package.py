# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamodrMl(RPackage):
	"""Detecting patterns of post-transcriptional modifications using machine learning

	RNAmodR.ML extend the functionality of the RNAmodR package and classical detection strategies towards detection through machine learning models. RNAmodR.ML provides classes, functions and an example workflow to establish a detection stratedy, which can be packaged.
	"""
	
	homepage = "https://github.com/FelixErnst/RNAmodR.ML"
	bioc = "RNAmodR.ML" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RNAmodR.ML_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RNAmodR.ML/RNAmodR.ML_1.16.0.tar.gz"]

	version("1.16.0", md5="b82e119e7d8c2387b22f4b38d0985970")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rnamodr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
