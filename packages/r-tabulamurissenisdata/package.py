# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabulamurissenisdata(RPackage):
	"""Bulk and single-cell RNA-seq data from the Tabula Muris Senis project

	This package provides access to RNA-seq data generated by the Tabula Muris Senis project via the Bioconductor project. The data is made available without restrictions by the Chan Zuckerberg Biohub. It is provided here without further processing, collected in the form of SingleCellExperiment objects.
	"""
	
	homepage = "https://github.com/fmicompbio/TabulaMurisSenisData"
	bioc = "TabulaMurisSenisData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/TabulaMurisSenisData_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/TabulaMurisSenisData/TabulaMurisSenisData_1.8.0.tar.gz"]

	version("1.8.0", md5="6d6120b18adce70e943a3da8e0e577b2")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

	# experiment