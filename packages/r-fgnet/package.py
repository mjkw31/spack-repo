# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgnet(RPackage):
	"""Functional Gene Networks derived from biological enrichment analyses

	Build and visualize functional gene and term networks from clustering of enrichment analyses in multiple annotation spaces. The package includes a graphical user interface (GUI) and functions to perform the functional enrichment analysis through DAVID, GeneTerm Linker, gage (GSEA) and topGO.
	"""
	
	homepage = "http://www.cicancer.org"
	bioc = "FGNet" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/FGNet_3.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/FGNet/FGNet_3.36.0.tar.gz"]

	version("3.36.0", md5="00da241d84bdc16ec9a8b1e27a3db509")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-igraph@0.6:", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
