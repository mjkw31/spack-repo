# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdesign3(RPackage):
	"""A unified framework of realistic in silico data generation and statistical model inference for single-cell and spatial omics

	We present a statistical simulator, scDesign3, to generate realistic single-cell and spatial omics data, including various cell states, experimental designs, and feature modalities, by learning interpretable parameters from real data. Using a unified probabilistic model for single-cell and spatial omics data, scDesign3 infers biologically meaningful parameters; assesses the goodness-of-fit of inferred cell clusters, trajectories, and spatial locations; and generates in silico negative and positive controls for benchmarking computational tools.
	"""
	
	homepage = "https://github.com/SONGDONGYUAN1994/scDesign3"
	bioc = "scDesign3" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scDesign3_1.0.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scDesign3/scDesign3_1.0.1.tar.gz"]

	version("1.0.1", md5="f4f74c0f98ede2f2560f556dfb14074a", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/scDesign3_1.0.1.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-rvinecopulib", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
