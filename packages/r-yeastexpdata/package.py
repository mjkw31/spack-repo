# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastexpdata(RPackage):
	"""Yeast Experimental Data

	A collection of different sets of experimental data from yeast.
	"""
	
	bioc = "yeastExpData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/yeastExpData_0.48.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/yeastExpData/yeastExpData_0.48.0.tar.gz"]

	version("0.48.0", md5="7cd63808a957defe831bf3e9d3ef4789")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-graph@1.9.26:", type=("build", "run"))

	# experiment