# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REwcedata(RPackage):
	"""The ewceData package provides reference data required for ewce

	This package provides reference data required for ewce. Expression Weighted Celltype Enrichment (EWCE) is used to determine which cell types are enriched within gene lists. The package provides tools for testing enrichments within simple gene lists (such as human disease associated genes) and those resulting from differential expression studies. The package does not depend upon any particular Single Cell Transcriptome dataset and user defined datasets can be loaded in and used in the analyses.
	"""
	
	homepage = "https://github.com/neurogenomics/ewceData"
	bioc = "ewceData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/ewceData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/ewceData/ewceData_1.10.0.tar.gz"]

	version("1.10.0", md5="d2ee91be35e2c5433ce16e94717c50e7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment