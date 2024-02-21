# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRseis(RPackage):
	"""Seismic Time Series Analysis Tools

	Multiple interactive codes to view and analyze seismic data, via spectrum analysis, wavelet transforms, particle motion, hodograms.  Includes general time-series tools, plotting, filtering, interactive display.
	"""
	
	cran = "RSEIS" 

	version("4.1-6", md5="42648affef3f08dabfbd8a9d908fc81e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rpmg", type=("build", "run"))
	depends_on("r-rwave", type=("build", "run"))
