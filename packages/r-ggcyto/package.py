# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgcyto(RPackage):
	"""Visualize Cytometry data with ggplot

	With the dedicated fortify method implemented for flowSet, ncdfFlowSet and GatingSet classes, both raw and gated flow cytometry data can be plotted directly with ggplot. ggcyto wrapper and some customed layers also make it easy to add gates and population statistics to the plot.
	"""
	
	homepage = "https://github.com/RGLab/ggcyto/issues"
	bioc = "ggcyto" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ggcyto_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ggcyto/ggcyto_1.30.0.tar.gz"]

	version("1.30.0", md5="f50828f54e40b73d30aa3ac0ef06de21")

	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-flowcore@1.41.5:", type=("build", "run"))
	depends_on("r-ncdfflow@2.17.1:", type=("build", "run"))
	depends_on("r-flowworkspace@4.13.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
