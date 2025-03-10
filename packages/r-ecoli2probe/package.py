# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoli2probe(RPackage):
	"""Probe sequence data for microarrays of type ecoli2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was E_coli_2_probe_tab.
	"""
	
	bioc = "ecoli2probe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ecoli2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ecoli2probe/ecoli2probe_2.18.0.tar.gz"]

	version("2.18.0", md5="061fcb782ee9da3aa5108881677a4531")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation