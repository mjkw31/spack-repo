# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbx20bamsubset(RPackage):
	"""Subset of BAM files from the "TBX20" experiment

	Dual transcriptional activator and repressor roles of TBX20 regulate adult cardiac structure and function. A subset of the RNA-Seq data.
	"""
	
	bioc = "TBX20BamSubset" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/TBX20BamSubset_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/TBX20BamSubset/TBX20BamSubset_1.38.0.tar.gz"]

	version("1.38.0", md5="c158901ec6203e85569c600efb335ccf")

	depends_on("r-rsamtools@1.9.8:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))

	# experiment