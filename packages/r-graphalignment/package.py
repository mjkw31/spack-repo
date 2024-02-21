# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphalignment(RPackage):
	"""GraphAlignment

	Graph alignment is an extension package for the R programming environment which provides functions for finding an alignment between two networks based on link and node similarity scores. (J. Berg and M. Laessig, "Cross-species analysis of biological networks by Bayesian alignment", PNAS 103 (29), 10967-10972 (2006))
	"""
	
	homepage = "http://www.thp.uni-koeln.de/~berg/GraphAlignment/"
	bioc = "GraphAlignment" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GraphAlignment_1.66.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GraphAlignment/GraphAlignment_1.66.0.tar.gz"]

	version("1.66.0", md5="0bc71a4722d0771d97671e81103bc8bb")

