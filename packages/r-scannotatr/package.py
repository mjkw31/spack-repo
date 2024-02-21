# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScannotatr(RPackage):
	"""Pretrained learning models for cell type prediction on single cell RNA-sequencing data

	The package comprises a set of pretrained machine learning models to predict basic immune cell types. This enables all users to quickly get a first annotation of the cell types present in their dataset without requiring prior knowledge. scAnnotatR also allows users to train their own models to predict new cell types based on specific research needs.
	"""
	
	homepage = "https://github.com/grisslab/scAnnotatR"
	bioc = "scAnnotatR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scAnnotatR_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scAnnotatR/scAnnotatR_1.8.0.tar.gz"]

	version("1.8.0", md5="5474e416000bda50dc8273a09b41a54b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
