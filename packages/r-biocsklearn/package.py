# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocsklearn(RPackage):
	"""interface to python sklearn via Rstudio reticulate

	This package provides interfaces to selected sklearn elements, and demonstrates fault tolerant use of python modules requiring extensive iteration.
	"""
	
	bioc = "BiocSklearn"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocSklearn_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocSklearn/BiocSklearn_1.24.0.tar.gz"]

	version("1.24.0", md5="a3df49031172bfd2b2a3b1c242b7dd40")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
	depends_on("py-scikit-learn", type=("build", "link", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
	depends_on("py-pandas", type=("build", "link", "run"))
	depends_on("py-h5py", type=("build", "link", "run"))
