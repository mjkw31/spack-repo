# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTenxvisiumdata(RPackage):
	"""Visium spatial gene expression data by 10X Genomics

	Collection of Visium spatial gene expression datasets by 10X Genomics, formatted into objects of class SpatialExperiment. Data cover various organisms and tissues, and include: single- and multi-section experiments, as well as single sections subjected to both whole transcriptome and targeted panel analysis. Datasets may be used for testing of and as examples in packages, for tutorials and workflow demonstrations, or similar purposes.
	"""
	
	homepage = "https://github.com/helenalc/TENxVisiumData"
	bioc = "TENxVisiumData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/TENxVisiumData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/TENxVisiumData/TENxVisiumData_1.10.0.tar.gz"]

	version("1.10.0", md5="f578add429847efff027a61b1749b9b4")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))

	# experiment