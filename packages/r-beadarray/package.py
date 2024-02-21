# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadarray(RPackage):
	"""Quality assessment and low-level analysis for Illumina BeadArray data

	The package is able to read bead-level data (raw TIFFs and text files) output by BeadScan as well as bead-summary data from BeadStudio. Methods for quality assessment and low-level analysis are provided.
	"""
	
	bioc = "beadarray" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/beadarray_2.52.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/beadarray/beadarray_2.52.0.tar.gz"]

	version("2.52.0", md5="ed1729be533d0731833e523174b9dbb4")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
	depends_on("r-biobase@2.17.8:", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-beaddatapackr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
