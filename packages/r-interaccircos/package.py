# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteraccircos(RPackage):
	"""The Generation of Interactive Circos Plot

	Implement in an efficient approach to display the genomic data, relationship, information in an interactive circular genome(Circos) plot. 'interacCircos' are inspired by 'circosJS', 'BioCircos.js' and 'NG-Circos' and we integrate the modules of 'circosJS', 'BioCircos.js' and 'NG-Circos' into this R package, based on 'htmlwidgets' framework.
	"""
	
	bioc = "interacCircos" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/interacCircos_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/interacCircos/interacCircos_1.12.0.tar.gz"]

	version("1.12.0", md5="d97429da8da823bf80547b4ac8ca2505")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
