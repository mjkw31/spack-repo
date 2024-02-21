# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaser(RPackage):
	"""Mapping Alternative Splicing Events to pRoteins

	This package provides functionalities for downstream analysis, annotation and visualizaton of alternative splicing events generated by rMATS.
	"""
	
	homepage = "https://github.com/DiogoVeiga/maser"
	bioc = "maser" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/maser_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/maser/maser_1.20.0.tar.gz"]

	version("1.20.0", md5="43be20847a05369476ccdb91cdd6ad4e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
