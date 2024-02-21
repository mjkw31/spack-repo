# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGagedata(RPackage):
	"""Auxillary data for gage package

	This is a supportive data package for the software package, gage. However, the data supplied here are also useful for gene set or pathway analysis or microarray data analysis in general. In this package, we provide two demo microarray dataset: GSE16873 (a breast cancer dataset from GEO) and BMP6 (originally published as an demo dataset for GAGE, also registered as GSE13604 in GEO). This package also includes commonly used gene set data based on KEGG pathways and GO terms for major research species, including human, mouse, rat and budding yeast. Mapping data between common gene IDs for budding yeast are also included.
	"""
	
	bioc = "gageData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/gageData_2.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/gageData/gageData_2.40.0.tar.gz"]

	version("2.40.0", md5="889e4b6ceda6c2a80f61ad4e867c3b59")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment