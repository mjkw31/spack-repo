# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZellkonverter(RPackage):
	"""Conversion Between scRNA-seq Objects

	Provides methods to convert between Python AnnData objects and SingleCellExperiment objects. These are primarily intended for use by downstream Bioconductor packages that wrap Python methods for single-cell data analysis. It also includes functions to read and write H5AD files used for saving AnnData objects to disk.
	"""
	
	homepage = "https://github.com/theislab/zellkonverter"
	bioc = "zellkonverter" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/zellkonverter_1.12.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/zellkonverter/zellkonverter_1.12.1.tar.gz"]

	version("1.12.1", md5="5ba05cd62d95057a39c194a5084c551a")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-singlecellexperiment@1.11.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
