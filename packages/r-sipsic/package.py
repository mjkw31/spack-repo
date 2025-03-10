# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSipsic(RPackage):
	"""Calculate Pathway Scores for Each Cell in scRNA-Seq Data

	Infer biological pathway activity of cells from single-cell RNA-sequencing data by calculating a pathway score for each cell (pathway genes are specified by the user). It is recommended to have the data in Transcripts-Per-Million (TPM) or Counts-Per-Million (CPM) units for best results. Scores may change when adding cells to or removing cells off the data. SiPSiC stands for Single Pathway analysis in Single Cells.
	"""
	
	homepage = "https://doi.org/10.1101/2023.03.27.534310"
	bioc = "SiPSiC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SiPSiC_1.2.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SiPSiC/SiPSiC_1.2.2.tar.gz"]

	version("1.2.2", md5="b8de9b61ecec686d20b8b3a4383cb6f9")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
