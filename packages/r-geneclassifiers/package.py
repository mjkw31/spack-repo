# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneclassifiers(RPackage):
	"""Application of gene classifiers

	This packages aims for easy accessible application of classifiers which have been published in literature using an ExpressionSet as input.
	"""
	
	homepage = "https://doi.org/doi:10.18129/B9.bioc.geneClassifiers"
	bioc = "geneClassifiers" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/geneClassifiers_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/geneClassifiers/geneClassifiers_1.26.0.tar.gz"]

	version("1.26.0", md5="79b7de2354913e5a91e6026f3f815a46")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
