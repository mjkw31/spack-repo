# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglecellsignalr(RPackage):
	"""Cell Signalling Using Single Cell RNAseq Data Analysis

	Allows single cell RNA seq data analysis, clustering, creates internal network and infers cell-cell interactions.
	"""
	
	bioc = "SingleCellSignalR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SingleCellSignalR_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SingleCellSignalR/SingleCellSignalR_1.14.0.tar.gz"]

	version("1.14.0", md5="d00060a859db9cd8c87ce9673cc9d886")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
