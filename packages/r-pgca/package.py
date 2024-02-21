# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgca(RPackage):
	"""PGCA: An Algorithm to Link Protein Groups Created from MS/MS Data

	Protein Group Code Algorithm (PGCA) is a computationally inexpensive algorithm to merge protein summaries from multiple experimental quantitative proteomics data. The algorithm connects two or more groups with overlapping accession numbers. In some cases, pairwise groups are mutually exclusive but they may still be connected by another group (or set of groups) with overlapping accession numbers. Thus, groups created by PGCA from multiple experimental runs (i.e., global groups) are called "connected" groups. These identified global protein groups enable the analysis of quantitative data available for protein groups instead of unique protein identifiers.
	"""
	
	bioc = "pgca" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/pgca_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/pgca/pgca_1.26.0.tar.gz"]

	version("1.26.0", md5="43c58c5b347ebf060a9e6afdc8aa8e93")

