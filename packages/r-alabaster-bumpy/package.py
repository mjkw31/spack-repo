# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterBumpy(RPackage):
	"""Save and Load BumpyMatrices to/from file

	Save BumpyMatrix objects into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.bumpy" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/alabaster.bumpy_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/alabaster.bumpy/alabaster.bumpy_1.2.0.tar.gz"]

	version("1.2.0", md5="0d5111cd74d5b72fc88eb66ac5b670c3")

	depends_on("r-bumpymatrix", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
