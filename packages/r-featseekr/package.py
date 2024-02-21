# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeatseekr(RPackage):
	"""FeatSeekR an R package for unsupervised feature selection

	FeatSeekR performs unsupervised feature selection using replicated measurements. It iteratively selects features with the highest reproducibility across replicates, after projecting out those dimensions from the data that are spanned by the previously selected features. The selected a set of features has a high replicate reproducibility and a high degree of uniqueness.
	"""
	
	homepage = "https://github.com/tcapraz/FeatSeekR"
	bioc = "FeatSeekR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/FeatSeekR_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/FeatSeekR/FeatSeekR_1.2.0.tar.gz"]

	version("1.2.0", md5="9792a703c1ec0b4a58c759274c2cb571")

	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
