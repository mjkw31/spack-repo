# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoe430bDb(RPackage):
	"""Affymetrix Affymetrix MOE430B Array annotation data (chip moe430b)

	Affymetrix Affymetrix MOE430B Array annotation data (chip moe430b) assembled using data from public repositories
	"""
	
	bioc = "moe430b.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/moe430b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/moe430b.db/moe430b.db_3.13.0.tar.gz"]

	version("3.13.0", md5="2d8a80b9d3342fb943087cc327c824e7")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation