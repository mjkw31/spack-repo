# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVenndetail(RPackage):
	"""A package for visualization and extract details

	A set of functions to generate high-resolution Venn,Vennpie plot,extract and combine details of these subsets with user datasets in data frame is available.
	"""
	
	homepage = "https://github.com/guokai8/VennDetail"
	bioc = "VennDetail" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/VennDetail_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/VennDetail/VennDetail_1.18.0.tar.gz"]

	version("1.18.0", md5="be9c3506e9707fe42642ea413c0873a6")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
