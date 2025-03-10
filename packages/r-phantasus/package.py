# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhantasus(RPackage):
	"""Visual and interactive gene expression analysis

	Phantasus is a web-application for visual and interactive gene expression analysis. Phantasus is based on Morpheus – a web-based software for heatmap visualisation and analysis, which was integrated with an R environment via OpenCPU API. Aside from basic visualization and filtering methods, R-based methods such as k-means clustering, principal component analysis or differential expression analysis with limma package are supported.
	"""
	
	homepage = "https://genome.ifmo.ru/phantasus"
	bioc = "phantasus" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/phantasus_1.22.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/phantasus/phantasus_1.22.2.tar.gz"]

	version("1.22.2", md5="84c6e2dce18e76a3268130cdd236ba59")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-protolite", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-rook", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-opencpu", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-fgsea@1.9.4:", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ccapp", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
