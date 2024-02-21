# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicp(RPackage):
	"""Harmonised Index of Consumer Prices

	The Harmonised Index of Consumer Prices (HICP) is the key economic figure to measure inflation in the euro area.
              The methodology underlying the HICP is documented in the HICP Methodological Manual (<https://ec.europa.eu/eurostat/de/web/products-manuals-and-guidelines/-/ks-gq-17-015>).
              Based on the manual, this package provides functions to access and work with HICP data from Eurostat's public database (<https://ec.europa.eu/eurostat/data/database>).
	"""
	
	homepage = "https://github.com/eurostat/hicp"
	cran = "hicp" 

	version("0.4.1", md5="3edca9249604e9ca4872662175ad30e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-restatapi@0.21:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
