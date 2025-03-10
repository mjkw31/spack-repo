# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyper(RPackage):
	"""An R Package For Geneset Enrichment Workflows

	An R Package for Geneset Enrichment Workflows.
	"""
	
	homepage = "https://github.com/montilab/hypeR"
	bioc = "hypeR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/hypeR_2.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/hypeR/hypeR_2.0.0.tar.gz"]

	version("2.0.0", md5="d2de417437ab81645e7d4702021f349f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
