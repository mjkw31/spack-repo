# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74bDb(RPackage):
	"""Affymetrix Affymetrix MG_U74B Array annotation data (chip mgu74b)

	Affymetrix Affymetrix MG_U74B Array annotation data (chip mgu74b) assembled using data from public repositories
	"""
	
	bioc = "mgu74b.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mgu74b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mgu74b.db/mgu74b.db_3.13.0.tar.gz"]

	version("3.13.0", md5="205577a6e41d56910f221ffb940ee25b")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation