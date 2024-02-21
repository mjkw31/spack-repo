# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPath2ppi(RPackage):
	"""Prediction of pathway-related protein-protein interaction networks

	Package to predict protein-protein interaction (PPI) networks in target organisms for which only a view information about PPIs is available. Path2PPI predicts PPI networks based on sets of proteins which can belong to a certain pathway from well-established model organisms. It helps to combine and transfer information of a certain pathway or biological process from several reference organisms to one target organism. Path2PPI only depends on the sequence similarity of the involved proteins.
	"""
	
	homepage = "http://www.bioinformatik.uni-frankfurt.de/"
	bioc = "Path2PPI" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Path2PPI_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Path2PPI/Path2PPI_1.32.0.tar.gz"]

	version("1.32.0", md5="4fcd4d73b05e2167ecdfb79aadfe8722")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
