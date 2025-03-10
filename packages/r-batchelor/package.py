# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchelor(RPackage):
	"""Single-Cell Batch Correction Methods

	Implements a variety of methods for batch correction of single-cell (RNA sequencing) data. This includes methods based on detecting mutually nearest neighbors, as well as several efficient variants of linear regression of the log-expression values. Functions are also provided to perform global rescaling to remove differences in depth between batches, and to perform a principal components analysis that is robust to differences in the numbers of cells across batches.
	"""
	
	bioc = "batchelor"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/batchelor_1.18.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/batchelor/batchelor_1.18.1.tar.gz"]

	version("1.18.1", md5="32763620ad2c6c3d0e168dd4fd1960be")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-residualmatrix", type=("build", "run"))
	depends_on("r-scaledmatrix", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
