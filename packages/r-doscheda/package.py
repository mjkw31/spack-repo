# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoscheda(RPackage):
	"""A DownStream Chemo-Proteomics Analysis Pipeline

	Doscheda focuses on quantitative chemoproteomics used to determine protein interaction profiles of small molecules from whole cell or tissue lysates using Mass Spectrometry data. The package provides a shiny application to run the pipeline, several visualisations and a downloadable report of an experiment.
	"""
	
	bioc = "Doscheda" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Doscheda_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Doscheda/Doscheda_1.24.0.tar.gz"]

	version("1.24.0", md5="3eee0480f798b00860daaf2cb88325ca")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-corrgram", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
