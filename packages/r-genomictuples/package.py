# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomictuples(RPackage):
	"""Representation and Manipulation of Genomic Tuples

	GenomicTuples defines general purpose containers for storing genomic tuples. It aims to provide functionality for tuples of genomic co-ordinates that are analogous to those available for genomic ranges in the GenomicRanges Bioconductor package.
	"""
	
	homepage = "www.github.com/PeteHaitch/GenomicTuples"
	bioc = "GenomicTuples" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GenomicTuples_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GenomicTuples/GenomicTuples_1.36.0.tar.gz"]

	version("1.36.0", md5="69e0c80982690604f35d9878f6640f37")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges@1.37.4:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.15.2:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-biocgenerics@0.21.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-iranges@2.19.13:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
