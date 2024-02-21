# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatplus(RPackage):
	"""Heatmaps with row and/or column covariates and colored clusters

	Display a rectangular heatmap (intensity plot) of a data matrix. By default, both samples (columns) and features (row) of the matrix are sorted according to a hierarchical clustering, and the corresponding dendrogram is plotted. Optionally, panels with additional information about samples and features can be added to the plot.
	"""
	
	homepage = "https://github.com/alexploner/Heatplus"
	bioc = "Heatplus" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Heatplus_3.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Heatplus/Heatplus_3.10.0.tar.gz"]

	version("3.10.0", md5="459fb0dbd1242699e9f394f156a7e0c1")

	depends_on("r-rcolorbrewer", type=("build", "run"))
