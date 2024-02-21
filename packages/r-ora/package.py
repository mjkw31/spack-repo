# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROra(RPackage):
	"""Convenient Tools for Working with Oracle Databases

	Easy-to-use functions to explore Oracle databases and import data
  into R. User interface for the ROracle package.
	"""
	
	cran = "ora"

	version("2.0-1", md5="4a6b7a39b80fe90f6170840a0f02c3c4")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-roracle", type=("build", "run"))
