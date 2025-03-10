# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmassbank(RPackage):
	"""Workflow to process tandem MS files and build MassBank records

	Workflow to process tandem MS files and build MassBank records. Functions include automated extraction of tandem MS spectra, formula assignment to tandem MS fragments, recalibration of tandem MS spectra with assigned fragments, spectrum cleanup, automated retrieval of compound information from Internet databases, and export to MassBank records.
	"""
	
	bioc = "RMassBank"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RMassBank_3.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RMassBank/RMassBank_3.12.0.tar.gz"]

	version("3.12.0", md5="59330cd723448b79eb751c6864e3dfbf")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rcdk", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-mzr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-envipat", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-readjdx", type=("build", "run"))
	depends_on("r-webchem", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
	depends_on("r-chemmineob", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("openbabel", type=("build", "link", "run"))
