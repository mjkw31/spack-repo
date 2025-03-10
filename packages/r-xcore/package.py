# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXcore(RPackage):
	"""xcore expression regulators inference

	xcore is an R package for transcription factor activity modeling based on known molecular signatures and user's gene expression data. Accompanying xcoredata package provides a collection of molecular signatures, constructed from publicly available ChiP-seq experiments. xcore use ridge regression to model changes in expression as a linear combination of molecular signatures and find their unknown activities. Obtained, estimates can be further tested for significance to select molecular signatures with the highest predicted effect on the observed expression changes.
	"""
	
	bioc = "xcore" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/xcore_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/xcore/xcore_1.6.0.tar.gz"]

	version("1.6.0", md5="4dd79b63bd7ff46aaa1b84dade889db2")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-delayedarray@0.18:", type=("build", "run"))
	depends_on("r-edger@3.34.1:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.44:", type=("build", "run"))
	depends_on("r-glmnet@4.1.2:", type=("build", "run"))
	depends_on("r-iranges@2.26:", type=("build", "run"))
	depends_on("r-iterators@1.0.13:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-matrix@1.3.4:", type=("build", "run"))
	depends_on("r-multiassayexperiment@1.18:", type=("build", "run"))
	depends_on("r-s4vectors@0.30:", type=("build", "run"))
