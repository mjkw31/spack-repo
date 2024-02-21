# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPigDb0(RPackage):
	"""Base Level Annotation databases for pig

	Base annotation databases for pig, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "pig.db0" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pig.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/pig.db0/pig.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="85aaccdbdb969825957db45db3fb7801", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pig.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation