# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeuratobject(RPackage):
	"""Data Structures for Single Cell Data.

	Defines S4 classes for single-cell genomic data and associated information,
	such as dimensionality reduction embeddings, nearest-neighbor graphs, and
	spatially-resolved coordinates. Provides data access methods and R-native
	hooks to ensure the Seurat object is familiar to other R users. See Satija
	R, Farrell J, Gennert D, et al (2015) <doi:10.1038/nbt.3192>, Macosko E,
	Basu A, Satija R, et al (2015) <doi:10.1016/j.cell.2015.05.002>, and Stuart
	T, Butler A, et al (2019) <doi:10.1016/j.cell.2019.05.031> for more
	details."""

	cran = "SeuratObject"

	version("5.0.1", md5="a1b6b337accbe962c59bd0f9cdf957e4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sp@1.5:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-matrix@1.6.3:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
