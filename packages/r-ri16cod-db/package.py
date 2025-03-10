# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRi16codDb(RPackage):
	"""Codelink Rat Inflammation 16 Bioarray annotation data (chip ri16cod)

	Codelink Rat Inflammation 16 Bioarray annotation data (chip ri16cod) assembled using data from public repositories
	"""
	
	bioc = "ri16cod.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ri16cod.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ri16cod.db/ri16cod.db_3.4.0.tar.gz"]

	version("3.4.0", md5="cd01b429295fdbba21dbe566effacbdd")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.2.1:", type=("build", "run"))

	# annotation