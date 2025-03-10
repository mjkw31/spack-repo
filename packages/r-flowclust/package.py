# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowclust(RPackage):
	"""Clustering for Flow Cytometry

	Robust model-based clustering using a t-mixture model with Box-Cox transformation. Note: users should have GSL installed. Windows users: 'consult the README file available in the inst directory of the source distribution for necessary configuration instructions'.
	"""
	
	bioc = "flowClust"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowClust_3.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowClust/flowClust_3.40.0.tar.gz"]

	version("3.40.0", md5="50e5d774ae44b8aaca69069733c175e3")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
