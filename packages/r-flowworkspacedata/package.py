# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowworkspacedata(RPackage):
	"""A data package containing two flowJo, one diva xml workspace and the associated fcs files as well as three GatingSets for testing the flowWorkspace, openCyto and CytoML packages.

	The necessary external data to run the flowWorkspace and openCyto vignette is found in this package.
	"""
	
	bioc = "flowWorkspaceData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/flowWorkspaceData_3.14.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/flowWorkspaceData/flowWorkspaceData_3.14.0.tar.gz"]

	version("3.14.0", md5="96655cef2a21f1b9d303ec775597a2dc")


	# experiment