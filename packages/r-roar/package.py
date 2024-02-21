# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoar(RPackage):
	"""Identify differential APA usage from RNA-seq alignments

	Identify preferential usage of APA sites, comparing two biological conditions, starting from known alternative sites and alignments obtained from standard RNA-seq experiments.
	"""
	
	homepage = "https://github.com/vodkatad/roar/"
	bioc = "roar" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/roar_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/roar/roar_1.38.0.tar.gz"]

	version("1.38.0", md5="563dcc245ffbc288c2e6ec9a9c138faa")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicalignments@0.99.4:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
