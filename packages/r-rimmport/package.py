# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRimmport(RPackage):
	"""RImmPort: Enabling Ready-for-analysis Immunology Research Data

	The RImmPort package simplifies access to ImmPort data for analysis in the R environment. It provides a standards-based interface to the ImmPort study data that is in a proprietary format.
	"""
	
	homepage = "http://bioconductor.org/packages/RImmPort/"
	bioc = "RImmPort" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RImmPort_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RImmPort/RImmPort_1.30.0.tar.gz"]

	version("1.30.0", md5="9a35da0a38439eee55d04ff8321ff09d")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
