# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74cDb(RPackage):
	"""Affymetrix Affymetrix MG_U74C Array annotation data (chip mgu74c)

	Affymetrix Affymetrix MG_U74C Array annotation data (chip mgu74c) assembled using data from public repositories
	"""
	
	bioc = "mgu74c.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mgu74c.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mgu74c.db/mgu74c.db_3.13.0.tar.gz"]

	version("3.13.0", md5="6c4f183e6ed5f0b5735596e7544746ae")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation