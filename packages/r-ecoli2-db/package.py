# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoli2Db(RPackage):
	"""Affymetrix Affymetrix E_coli_2 Array annotation data (chip ecoli2)

	Affymetrix Affymetrix E_coli_2 Array annotation data (chip ecoli2) assembled using data from public repositories
	"""
	
	bioc = "ecoli2.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ecoli2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ecoli2.db/ecoli2.db_3.13.0.tar.gz"]

	version("3.13.0", md5="110d6549b1d105fdff31ab8f45b08d65")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-eck12-eg-db@3.13:", type=("build", "run"))

	# annotation