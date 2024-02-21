# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgoslin(RPackage):
	"""Lipid Shorthand Name Parsing and Normalization

	The R implementation for the Grammar of Succint Lipid Nomenclature parses different short hand notation dialects for lipid names. It normalizes them to a standard name. It further provides calculated monoisotopic masses and sum formulas for each successfully parsed lipid name and supplements it with LIPID MAPS Category and Class information. Also, the structural level and further structural details about the head group, fatty acyls and functional groups are returned, where applicable.
	"""
	
	homepage = "https://github.com/lifs-tools/rgoslin"
	bioc = "rgoslin" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rgoslin_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rgoslin/rgoslin_1.6.0.tar.gz"]

	version("1.6.0", md5="211ef77e63cc8394ebc5eee33328cd08")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
