# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpaniel(RPackage):
	"""Spatial Transcriptomics Analysis

	Spaniel includes a series of tools to aid the quality control and analysis of Spatial Transcriptomics data. Spaniel can import data from either the original Spatial Transcriptomics system or 10X Visium technology. The package contains functions to create a SingleCellExperiment Seurat object and provides a method of loading a histologial image into R. The spanielPlot function allows visualisation of metrics contained within the S4 object overlaid onto the image of the tissue.
	"""
	
	bioc = "Spaniel" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Spaniel_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Spaniel/Spaniel_1.16.0.tar.gz"]

	version("1.16.0", md5="fb29666756a1db567f16b5c72420de4c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scater@1.13:", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dropletutils", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
