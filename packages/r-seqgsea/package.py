# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqgsea(RPackage):
	"""Gene Set Enrichment Analysis (GSEA) of RNA-Seq Data: integrating differential expression and splicing

	The package generally provides methods for gene set enrichment analysis of high-throughput RNA-Seq data by integrating differential expression and splicing. It uses negative binomial distribution to model read count data, which accounts for sequencing biases and biological variation. Based on permutation tests, statistical significance can also be achieved regarding each gene's differential expression and splicing, respectively.
	"""
	
	bioc = "SeqGSEA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SeqGSEA_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SeqGSEA/SeqGSEA_1.42.0.tar.gz"]

	version("1.42.0", md5="13213924066a18535220d42938e923fa")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
