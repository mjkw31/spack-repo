# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWiggleplotr(RPackage):
	"""Make read coverage plots from BigWig files

	Tools to visualise read coverage from sequencing experiments together with genomic annotations (genes, transcripts, peaks). Introns of long transcripts can be rescaled to a fixed length for better visualisation of exonic read coverage.
	"""
	
	bioc = "wiggleplotr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/wiggleplotr_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/wiggleplotr/wiggleplotr_1.26.0.tar.gz"]

	version("1.26.0", md5="9e05d485ba51bf035918d23e686e60ba")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
