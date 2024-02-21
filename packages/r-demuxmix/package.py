# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemuxmix(RPackage):
	"""Demultiplexing oligo-barcoded scRNA-seq data using regression mixture models

	A package for demultiplexing single-cell sequencing experiments of pooled cells labeled with barcode oligonucleotides. The package implements methods to fit regression mixture models for a probabilistic classification of cells, including multiplet detection. Demultiplexing error rates can be estimated, and methods for quality control are provided.
	"""
	
	homepage = "https://github.com/huklein/demuxmix"
	bioc = "demuxmix" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/demuxmix_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/demuxmix/demuxmix_1.4.0.tar.gz"]

	version("1.4.0", md5="9bbdcc634e542fe151a50a2511206140")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
