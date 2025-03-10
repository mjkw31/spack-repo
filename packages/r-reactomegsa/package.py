# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactomegsa(RPackage):
	"""Client for the Reactome Analysis Service for comparative multi-omics gene set analysis

	The ReactomeGSA packages uses Reactome's online analysis service to perform a multi-omics gene set analysis. The main advantage of this package is, that the retrieved results can be visualized using REACTOME's powerful webapplication. Since Reactome's analysis service also uses R to perfrom the actual gene set analysis you will get similar results when using the same packages (such as limma and edgeR) locally. Therefore, if you only require a gene set analysis, different packages are more suited.
	"""
	
	homepage = "https://github.com/reactome/ReactomeGSA"
	bioc = "ReactomeGSA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ReactomeGSA_1.16.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ReactomeGSA/ReactomeGSA_1.16.1.tar.gz"]

	version("1.16.1", md5="c4ef9b68baf6957b7a3abf38bd4ffb39")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
