# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractivedisplay(RPackage):
	"""Package for enabling powerful shiny web displays of Bioconductor objects

	The interactiveDisplay package contains the methods needed to generate interactive Shiny based display methods for Bioconductor objects.
	"""
	
	bioc = "interactiveDisplay" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/interactiveDisplay_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/interactiveDisplay/interactiveDisplay_1.40.0.tar.gz"]

	version("1.40.0", md5="4adec73e763df3dc2e697e41bff3ead8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-interactivedisplaybase@1.7.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gridsvg", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-category", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
