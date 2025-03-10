# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubcDb(RPackage):
	"""Affymetrix Affymetrix Hu35KsubC Array annotation data (chip hu35ksubc)

	Affymetrix Affymetrix Hu35KsubC Array annotation data (chip hu35ksubc) assembled using data from public repositories
	"""
	
	bioc = "hu35ksubc.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hu35ksubc.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hu35ksubc.db/hu35ksubc.db_3.13.0.tar.gz"]

	version("3.13.0", md5="57e60b8d025e0e8cf7ac2b355111cf2d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation