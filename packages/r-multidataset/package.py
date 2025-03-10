# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultidataset(RPackage):
	"""Implementation of MultiDataSet and ResultSet

	Implementation of the BRGE's (Bioinformatic Research Group in Epidemiology from Center for Research in Environmental Epidemiology) MultiDataSet and ResultSet. MultiDataSet is designed for integrating multi omics data sets and ResultSet is a container for omics results. This package contains base classes for MEAL and rexposome packages.
	"""
	
	bioc = "MultiDataSet" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MultiDataSet_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MultiDataSet/MultiDataSet_1.30.0.tar.gz"]

	version("1.30.0", md5="304e6d8ccbb54c446f43f2df5e13f530")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
