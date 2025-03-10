# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdamgui(RPackage):
	"""Activity and Diversity Analysis Module Graphical User Interface

	ADAMgui is a Graphical User Interface for the ADAM package. The ADAMgui package provides 2 shiny-based applications that allows the user to study the output of the ADAM package files through different plots. It's possible, for example, to choose a specific GFAG and observe the gene expression behavior with the plots created with the GFAGtargetUi function. Features such as differential expression and foldchange can be easily seen with aid of the plots made with GFAGpathUi function.
	"""
	
	homepage = "TBA"
	bioc = "ADAMgui" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ADAMgui_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ADAMgui/ADAMgui_1.18.0.tar.gz"]

	version("1.18.0", md5="d6b76d93be7f193cd913f44f6ff41a64")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-adam", type=("build", "run"))
	depends_on("r-go-db@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-shiny@1.1:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-stringi@1.2.4:", type=("build", "run"))
	depends_on("r-varhandle@2.0.3:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-ggpubr@0.1.8:", type=("build", "run"))
	depends_on("r-ggsignif@0.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-colorramps@2.3:", type=("build", "run"))
	depends_on("r-dt@0.4:", type=("build", "run"))
	depends_on("r-data-table@1.11.4:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-shinyjs@1:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
