# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH20kcodDb(RPackage):
	"""Codelink UniSet Human 20k I Bioarray annotation data (chip h20kcod)

	Codelink UniSet Human 20k I Bioarray annotation data (chip h20kcod) assembled using data from public repositories
	"""
	
	bioc = "h20kcod.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/h20kcod.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/h20kcod.db/h20kcod.db_3.4.0.tar.gz"]

	version("3.4.0", md5="3647facb272f58424f4c94ef92e8ee45")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.2.1:", type=("build", "run"))

	# annotation