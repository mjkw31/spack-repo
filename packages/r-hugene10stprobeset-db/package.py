# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene10stprobesetDb(RPackage):
	"""Affymetrix hugene10 annotation data (chip hugene10stprobeset)

	Affymetrix hugene10 annotation data (chip hugene10stprobeset) assembled using data from public repositories
	"""
	
	bioc = "hugene10stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hugene10stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hugene10stprobeset.db/hugene10stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="0a4a87d64564cbec1e4bb1f9e5a67add")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation