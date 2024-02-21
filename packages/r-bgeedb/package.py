# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgeedb(RPackage):
	"""Annotation and gene expression data retrieval from Bgee database. TopAnat, an anatomical entities Enrichment Analysis tool for UBERON ontology

	A package for the annotation and gene expression data download from Bgee database, and TopAnat analysis: GO-like enrichment of anatomical terms, mapped to genes by expression patterns.
	"""
	
	homepage = "https://github.com/BgeeDB/BgeeDB_R"
	bioc = "BgeeDB" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BgeeDB_2.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BgeeDB/BgeeDB_2.28.0.tar.gz"]

	version("2.28.0", md5="9b8f5e9e829bd05d9a8322b3ff3408dd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
