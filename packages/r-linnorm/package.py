# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinnorm(RPackage):
	"""Linear model and normality based normalization and transformation method (Linnorm)

	Linnorm is an algorithm for normalizing and transforming RNA-seq, single cell RNA-seq, ChIP-seq count data or any large scale count data. It has been independently reviewed by Tian et al. on Nature Methods (https://doi.org/10.1038/s41592-019-0425-8). Linnorm can work with raw count, CPM, RPKM, FPKM and TPM.
	"""
	
	homepage = "https://doi.org/10.1093/nar/gkx828"
	bioc = "Linnorm" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Linnorm_2.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Linnorm/Linnorm_2.26.0.tar.gz"]

	version("2.26.0", md5="8fc0ff0d6e9c2d274137b0e99ce0f4a2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
