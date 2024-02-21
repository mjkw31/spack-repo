# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartheenmetadataDb(RPackage):
	"""PartheenMetaData http://swegene.onk.lu.se Annotation Data (PartheenMetaData)

	PartheenMetaData http://swegene.onk.lu.se Annotation Data (PartheenMetaData) assembled using data from public repositories
	"""
	
	bioc = "PartheenMetaData.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/PartheenMetaData.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/PartheenMetaData.db/PartheenMetaData.db_3.2.3.tar.gz"]

	version("3.2.3", md5="1c9fd27e13a341b9aba9a235a67ce978")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation