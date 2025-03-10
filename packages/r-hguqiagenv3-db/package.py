# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHguqiagenv3Db(RPackage):
	"""Qiagen Qiagen V3.0 oligo set annotation data (chip hguqiagenv3)

	Qiagen Qiagen V3.0 oligo set annotation data (chip hguqiagenv3) assembled using data from public repositories
	"""
	
	bioc = "hguqiagenv3.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hguqiagenv3.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hguqiagenv3.db/hguqiagenv3.db_3.2.3.tar.gz"]

	version("3.2.3", md5="91ebb82e773ff799befdb8921b38e90e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation