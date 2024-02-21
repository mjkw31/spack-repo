# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialheatmap(RPackage):
	"""spatialHeatmap

	The spatialHeatmap package offers the primary functionality for visualizing cell-, tissue- and organ-specific assay data in spatial anatomical images. Additionally, it provides extended functionalities for large-scale data mining routines and co-visualizing bulk and single-cell data.
	"""
	
	homepage = "https://github.com/jianhaizhang/spatialHeatmap"
	bioc = "spatialHeatmap" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/spatialHeatmap_2.8.4.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/spatialHeatmap/spatialHeatmap_2.8.4.tar.gz"]

	version("2.8.4", md5="70521209d8c691ef6dac895936ee3227")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-grimport", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-spscomps@0.3.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
