# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsealm(RPackage):
	"""Linear Model Toolset for Gene Set Enrichment Analysis

	Models and methods for fitting linear models to gene expression data, together with tools for computing and using various regression diagnostics.
	"""
	
	bioc = "GSEAlm" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GSEAlm_1.62.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GSEAlm/GSEAlm_1.62.0.tar.gz"]

	version("1.62.0", md5="b88623d080b75bb6775026e9e6c4dd9e")

	depends_on("r-biobase", type=("build", "run"))
