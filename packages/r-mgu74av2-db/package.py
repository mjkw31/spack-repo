# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74av2Db(RPackage):
	"""Affymetrix Affymetrix MG_U74Av2 Array annotation data (chip mgu74av2)

	Affymetrix Affymetrix MG_U74Av2 Array annotation data (chip mgu74av2) assembled using data from public repositories
	"""
	
	bioc = "mgu74av2.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mgu74av2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mgu74av2.db/mgu74av2.db_3.13.0.tar.gz"]

	version("3.13.0", md5="3205856d0c7725acded5238415e907bc")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation