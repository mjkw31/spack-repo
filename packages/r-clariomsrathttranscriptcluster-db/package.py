# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomsrathttranscriptclusterDb(RPackage):
	"""Affymetrix clariomsratht annotation data (chip clariomsrathttranscriptcluster)

	Affymetrix clariomsratht annotation data (chip clariomsrathttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "clariomsrathttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/clariomsrathttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/clariomsrathttranscriptcluster.db/clariomsrathttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="e7c71721f8201bfd1553a98cfbf47458")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation