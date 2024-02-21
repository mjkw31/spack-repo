# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDta(RPackage):
	"""Dynamic Transcriptome Analysis

	Dynamic Transcriptome Analysis (DTA) can monitor the cellular response to perturbations with higher sensitivity and temporal resolution than standard transcriptomics. The package implements the underlying kinetic modeling approach capable of the precise determination of synthesis- and decay rates from individual microarray or RNAseq measurements.
	"""
	
	bioc = "DTA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DTA_2.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DTA/DTA_2.48.0.tar.gz"]

	version("2.48.0", md5="58705aacdbf08c61d4713273dbd9bc6f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lsd", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
