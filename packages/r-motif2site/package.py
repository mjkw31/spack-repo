# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotif2site(RPackage):
	"""Detect binding sites from motifs and ChIP-seq experiments, and compare binding sites across conditions

	Detect binding sites using motifs IUPAC sequence or bed coordinates and ChIP-seq experiments in bed or bam format. Combine/compare binding sites across experiments, tissues, or conditions. All normalization and differential steps are done using TMM-GLM method. Signal decomposition is done by setting motifs as the centers of the mixture of normal distribution curves.
	"""
	
	bioc = "Motif2Site" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Motif2Site_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Motif2Site/Motif2Site_1.6.0.tar.gz"]

	version("1.6.0", md5="e8228f1deb42f2d4b3867a90a6eba14c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
