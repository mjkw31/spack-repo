# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuex10StV2frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type huex.1.0.st.v2

	This package was created by frmaTools version 1.9.2.
	"""
	
	bioc = "huex.1.0.st.v2frmavecs" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/huex.1.0.st.v2frmavecs_1.1.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/huex.1.0.st.v2frmavecs/huex.1.0.st.v2frmavecs_1.1.0.tar.gz"]

	version("1.1.0", md5="982935d07b526ff555790e309fe4147e")

	depends_on("r@2.10:", type=("build", "run"))

	# annotation