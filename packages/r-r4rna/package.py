# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR4rna(RPackage):
	"""An R package for RNA visualization and analysis

	A package for RNA basepair analysis, including the visualization of basepairs as arc diagrams for easy comparison and annotation of sequence and structure.  Arc diagrams can additionally be projected onto multiple sequence alignments to assess basepair conservation and covariation, with numerical methods for computing statistics for each.
	"""
	
	homepage = "http://www.e-rna.org/r-chie/"
	bioc = "R4RNA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/R4RNA_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/R4RNA/R4RNA_1.30.0.tar.gz"]

	version("1.30.0", md5="a77903559307ab481671650646dd85e5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.38:", type=("build", "run"))
