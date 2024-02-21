# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNebulosa(RPackage):
	"""Single-Cell Data Visualisation Using Kernel Gene-Weighted Density Estimation

	This package provides a enhanced visualization of single-cell data based on gene-weighted density estimation. Nebulosa recovers the signal from dropped-out features and allows the inspection of the joint expression from multiple features (e.g. genes). Seurat and SingleCellExperiment objects can be used within Nebulosa.
	"""
	
	homepage = "https://github.com/powellgenomicslab/Nebulosa"
	bioc = "Nebulosa" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Nebulosa_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Nebulosa/Nebulosa_1.12.0.tar.gz"]

	version("1.12.0", md5="e71c21bbda87365578a49f21dd915fa4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
