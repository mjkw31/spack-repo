# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsensus(RPackage):
	"""Cross-platform consensus analysis of genomic measurements via interlaboratory testing method

	An implementation of the American Society for Testing and Materials (ASTM) Standard E691 for interlaboratory testing procedures, designed for cross-platform genomic measurements. Given three (3) or more genomic platforms or laboratory protocols, this package provides interlaboratory testing procedures giving per-locus comparisons for sensitivity and precision between platforms.
	"""
	
	bioc = "consensus" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/consensus_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/consensus/consensus_1.20.0.tar.gz"]

	version("1.20.0", md5="f930fc9b058bce80ccbb112082cf3dc7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
