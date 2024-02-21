# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprviz(RPackage):
	"""Visualization Functions for CRISPR gRNAs

	Provides functionalities to visualize and contextualize CRISPR guide RNAs (gRNAs) on genomic tracks across nucleases and applications. Works in conjunction with the crisprBase and crisprDesign Bioconductor packages. Plots are produced using the Gviz framework.
	"""
	
	homepage = "https://github.com/crisprVerse/crisprViz"
	bioc = "crisprViz" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/crisprViz_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/crisprViz/crisprViz_1.4.0.tar.gz"]

	version("1.4.0", md5="a95c0cc87c7934da1e9bbfeb1e27bd3a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-crisprbase@0.99.15:", type=("build", "run"))
	depends_on("r-crisprdesign@0.99.77:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
