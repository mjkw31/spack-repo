# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanoporernaseq(RPackage):
	"""Nanopore RNA-Seq Example data

	The NanoporeRNASeq package contains long read RNA-Seq data generated using Oxford Nanopore Sequencing. The data consists of 6 samples from two human cell lines (K562 and MCF7) that were generated by the SG-NEx project. Each of these cell lines has three replicates, with 1 direct RNA sequencing data and 2 cDNA sequencing data. Reads are aligned to chromosome 22 (Grch38) and stored as bam files. The original data is from the SG-NEx project.
	"""
	
	homepage = "https://github.com/GoekeLab/NanoporeRNASeq"
	bioc = "NanoporeRNASeq" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/NanoporeRNASeq_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/NanoporeRNASeq/NanoporeRNASeq_1.12.0.tar.gz"]

	version("1.12.0", md5="eca12ebcd403efd53e1b38d5f03f2027")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-experimenthub@1.15.3:", type=("build", "run"))

	# experiment