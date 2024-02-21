# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMalariaDb0(RPackage):
	"""Base Level Annotation databases for malaria

	Base annotation databases for malaria, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "malaria.db0" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/malaria.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/malaria.db0/malaria.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="6f71b4ac69ae5237f3f5e1337d5073d7", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/malaria.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation