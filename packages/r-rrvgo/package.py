# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrvgo(RPackage):
	"""Reduce + Visualize GO

	Reduce and visualize lists of Gene Ontology terms by identifying redudance based on semantic similarity.
	"""
	
	homepage = "https://www.bioconductor.org/packages/rrvgo"
	bioc = "rrvgo" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rrvgo_1.14.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rrvgo/rrvgo_1.14.1.tar.gz"]

	version("1.14.1", md5="b1813722d66dba8b701c0cc0f614c5ca")

	depends_on("r-gosemsim", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-treemap", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
