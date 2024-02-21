# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPviz(RPackage):
	"""Peptide Annotation and Data Visualization using Gviz

	Pviz adapts the Gviz package for protein sequences and data.
	"""
	
	bioc = "Pviz" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Pviz_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Pviz/Pviz_1.36.0.tar.gz"]

	version("1.36.0", md5="1a1513067c6a873f9523f20eb85f2878")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gviz@1.7.10:", type=("build", "run"))
	depends_on("r-biovizbase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
