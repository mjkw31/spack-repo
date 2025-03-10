# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffylmgui(RPackage):
	"""GUI for limma Package with Affymetrix Microarrays

	A Graphical User Interface (GUI) for analysis of Affymetrix microarray gene expression data using the affy and limma packages.
	"""
	
	homepage = "http://bioinf.wehi.edu.au/affylmGUI/"
	bioc = "affylmGUI" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/affylmGUI_1.76.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/affylmGUI/affylmGUI_1.76.0.tar.gz"]

	version("1.76.0", md5="22d9ba796444840fc24cf9b7384f81c9")

	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-affyio", type=("build", "run"))
	depends_on("r-affyplm", type=("build", "run"))
	depends_on("r-gcrma", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
