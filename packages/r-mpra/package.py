# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpra(RPackage):
	"""Analyze massively parallel reporter assays

	Tools for data management, count preprocessing, and differential analysis in massively parallel report assays (MPRA).
	"""
	
	homepage = "https://github.com/hansenlab/mpra"
	bioc = "mpra" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mpra_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mpra/mpra_1.24.0.tar.gz"]

	version("1.24.0", md5="ee3c8c16534188d568ee8f0e01afb894")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
