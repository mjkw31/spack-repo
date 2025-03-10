# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedbarrayv10Db(RPackage):
	"""FHCRC Nelson Lab pedbarrayv10 Annotation Data (pedbarrayv10)

	FHCRC Nelson Lab pedbarrayv10 Annotation Data (pedbarrayv10) assembled using data from public repositories
	"""
	
	bioc = "pedbarrayv10.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pedbarrayv10.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/pedbarrayv10.db/pedbarrayv10.db_3.2.3.tar.gz"]

	version("3.2.3", md5="25acc3bfee229015ecca1c7d688e5168")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation