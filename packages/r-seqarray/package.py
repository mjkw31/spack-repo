# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqarray(RPackage):
	"""Data Management of Large-Scale Whole-Genome Sequence Variant Calls

	Data management of large-scale whole-genome sequencing variant calls with thousands of individuals: genotypic data (e.g., SNVs, indels and structural variation calls) and annotations in SeqArray GDS files are stored in an array-oriented and compressed manner, with efficient data access using the R programming language.
	"""
	
	homepage = "https://github.com/zhengxwen/SeqArray"
	bioc = "SeqArray" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SeqArray_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SeqArray/SeqArray_1.42.0.tar.gz"]

	version("1.42.0", md5="9754225574380705e505629db229d41a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
