# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProjectr(RPackage):
	"""Functions for the projection of weights from PCA, CoGAPS, NMF, correlation, and clustering

	Functions for the projection of data into the spaces defined by PCA, CoGAPS, NMF, correlation, and clustering.
	"""
	
	homepage = "https://github.com/genesofeve/projectR/"
	bioc = "projectR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/projectR_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/projectR/projectR_1.18.0.tar.gz"]

	version("1.18.0", md5="7351d9a1c593186a6adb189ebd3ff9d2")

	depends_on("r@4.0.1:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-ggalluvial", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-tsne", type=("build", "run"))
