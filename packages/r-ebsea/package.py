# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbsea(RPackage):
	"""Exon Based Strategy for Expression Analysis of genes

	Calculates differential expression of genes based on exon counts of genes obtained from RNA-seq sequencing data.
	"""
	
	bioc = "EBSEA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/EBSEA_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/EBSEA/EBSEA_1.30.0.tar.gz"]

	version("1.30.0", md5="d016b1e83c4b885565a573db1b134fbd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-empiricalbrownsmethod", type=("build", "run"))
